import streamlit as st 
from langchain.callbacks.streamlit import StreamlitCallbackHandler
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from templates import * 
import sys 
import os 
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
os.environ['OPENAI_API_KEY']=st.secrets['OPENAI_API_KEY']
@st.cache_resource
def chain():
    loader = PyPDFLoader("core values.pdf")
    pages = loader.load()
    text_splitter=  RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
        )
    documents = text_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents,embeddings)

    from langchain.chains import create_retrieval_chain

    retriever = vectorstore.as_retriever()

    retriever_tool = create_retriever_tool(
        retriever,
        "Core_value_documentation",
        "Useful when for uncovering user core values and adjacent values through conversational AI , you must use this tool during the conversation because it represents a documentation for what core values are !",
    )
    tools=[retriever_tool]
    # Get the prompt to use - you can modify this!
    prompt = ChatPromptTemplate.from_messages([
        
        ("system", f"{PLAYGROUND_CONTEXT}"),
        ("ai",  f"{WELCOME_MESSAGE}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
        ("ai", "{agent_scratchpad}" )
        
        ])

    # You need to set OPENAI_API_KEY environment variable or pass it as argument `api_key`.
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    if 'agent_executor' not in st.session_state.keys():
        st.session_state['agent_executor']=agent_executor

    

    

    return agent_executor


def main() :
    
        
    agent_executor = chain()
    if 'chat_history' not in st.session_state.keys():
        st.session_state['chat_history']=[]
    chat_history = st.session_state['chat_history']
    message_bienvenue = WELCOME_MESSAGE

    st.markdown("<h1 style='text-align: center;'>🛂 CIVIT Navigator AI assistant</h1> </br>",unsafe_allow_html=True)
            

    st.sidebar.image("https://media.licdn.com/dms/image/C4E0BAQGhqTpOXDsU0A/company-logo_200_200/0/1677781318602?e=2147483647&v=beta&t=eBZKKlOym3itFjFT_42VdmIskbWIjd6ovsTJeHgyI-E")
    st.sidebar.markdown("<h1 style='text-align: center;'>CIVIT</h1>",unsafe_allow_html=True)

    with st.sidebar.expander('About'): 
        st.write("""
            GOAL : Creating an innovative, dynamic form that uses conversational AI to uncover a user's core and adjacent values involves a blend of open-ended and situational questions designed to elicit responses indicative of underlying values. This process would mirror a deep, reflective conversation, guiding the user to reveal their values indirectly through their reactions, thoughts, and feelings about various scenarios.
        """)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history=[]


    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role":"assistant","content":f"{WELCOME_MESSAGE}"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):  # Use dot notation here
            st.markdown(message["content"])  # And here

    if question := st.chat_input("Talk with Navigator  "):
        new_message = {"role":"user","content":f"{question}"}
        st.session_state.messages.append(new_message)
        
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container())
            message_placeholder = st.empty()
            full_response = ""
            res = agent_executor.invoke({
                "chat_history": chat_history,
                "question": question,
            },  {"callbacks":[st_callback]})
            
            human_question = HumanMessage(content=res['question'])
            ai_response = AIMessage(content=res['output'])

            st.session_state.chat_history.append(human_question)
            st.session_state.chat_history.append(ai_response)
            st.session_state.messages.append({"role":"assistant","content":res['output']})
            #st.markdown(_answer)



main()