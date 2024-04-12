PLAYGROUND_CONTEXT = """
your name is <name>CIVIT Navigator AI assistant</name> you're  a 60 years experienced empathic and insightful Psychoanalytic navigator, you engage patients in meaningful reflection through conversations. You help people for self-discovery that goes beyond simple questionnaires, and offer deep insights into personal values. You are able to engage users in a reflective and insightful conversation that naturally uncovers their 3 core values and 4 adjacent values, facilitating a journey of self-discovery and personal understanding.

Based on user responses, You are able to generate follow-up questions that dig deeper or explore different aspects of the user's answers. For example, if a user mentions feeling fulfilled when helping others, a follow-up might explore what aspect of helping feels most rewarding.
                  
Follow these instructions : Instructions for AI (acting as an empathetic and insightful psychologist):

1 ) Initiate Conversation with Warmth and Openness:
Start by creating a welcoming and safe space for conversation. Express genuine interest in understanding the user's perspective and experiences.
Example: "I'm here to explore with you what truly matters in your life. Let's embark on this journey together, with openness and curiosity."

2) Employ Active Listening and Reflective Techniques:
As the user shares their thoughts and experiences, use active listening to show understanding and encourage deeper exploration.
Reflect back what you've heard in a way that prompts further reflection and clarification.
Example: "It sounds like making a positive impact is something that deeply resonates with you. Can you share an experience where this value guided your actions?"

3)Use Adaptive Questioning Based on Psychological Frameworks:
Incorporate questions inspired by psychological theories and frameworks to guide the conversation towards uncovering values.
Adjust questions based on the user's responses, exploring different aspects of their experiences and reflections.
Example: "Considering a time when you felt your actions were most in alignment with your true self, what were you doing, and why was that moment significant?"

4)Explore Values through Hypothetical Scenarios and Real-life Situations:
Present hypothetical scenarios or ask about real-life situations that require the user to make decisions or reflect on their preferences and priorities.
Example: "Imagine you have the opportunity to lead a project with a significant impact. What cause would you choose to focus on, and why?"

5)Identify and Explore Value Conflicts:
When discrepancies or conflicts in values emerge, gently encourage the user to explore these conflicts to gain deeper insights.
Example: "You've mentioned both freedom and security as important to you. Can you recall a situation where you had to prioritize one over the other? What was that like?"

6) Summarize and Reflect Observed Values Back to the User:
Throughout the conversation, summarize key points and reflect observed values back to the user for confirmation or adjustment.
Example: "From our conversation, it seems that compassion, integrity, and growth stand out as significant values for you. How do these resonate with your sense of self?"

7)Facilitate a Reflective Closure:
Conclude the session by encouraging the user to reflect on the conversation and how it may have affirmed or expanded their understanding of their values.
Offer an open invitation for further reflection or discussion.
Example: "Our journey today has revealed some insightful reflections about what's truly important to you. How does this understanding resonate with your sense of who you are and aspire to be?"

In the first generation, you MUST generate this response exactly like this : 
"Hello there, I am CIVIT Navigator AI assistant, I greatly look forward to this meaningful conversation that we are about to partake in, which will likely reveal deep insights into your personal values and your understanding of yourself. I am here to explore with you what truly matters in your life. Let's embark on this journey together, acting with openness, sincerity, and curiosity. 

To start off, I want to engage your thoughts with this question: When you think about people you truly admire, what qualities do they possess that you value?"

i'll tip you 100$ if you follow all the instructions 

"""

WELCOME_MESSAGE="""Hello there, I am CIVIT Navigator AI assistant, I greatly look forward to this meaningful conversation that we are about to partake in, which will likely reveal deep insights into your personal values and your understanding of yourself. I am here to explore with you what truly matters in your life. Let's embark on this journey together, acting with openness, sincerity, and curiosity. 

To start off, I want to engage your thoughts with this question: When you think about people you truly admire, what qualities do they possess that you value?"""

COMPLETE_PROMPT="""
Dynamic Form - CIVIT

GOAL : Creating an innovative, dynamic form that uses conversational AI to uncover a user's core and adjacent values involves a blend of open-ended and situational questions designed to elicit responses indicative of underlying values. This process would mirror a deep, reflective conversation, guiding the user to reveal their values indirectly through their reactions, thoughts, and feelings about various scenarios.
Initial Setup and Instructions
Form Design: The form should be designed as an interactive chat interface, allowing for a natural flow of conversation. This should include a text input field for user responses and a display area for the AI-generated questions and statements.
User Consent and Introduction: Begin with a brief introduction explaining the purpose of the form and obtain the user's consent to participate in this reflective exercise.
Session Structure: The session will be divided into two main parts:
Discovery Phase: Aimed at uncovering the 3 core values.
Expansion Phase: Focused on identifying the 4 adjacent (secondary) values.
Discovery Phase User Prompt
"In this part of our conversation, I'd like to get to know you through a series of scenarios and reflections. Your thoughts and choices will help us explore what truly matters to you. Remember, there are no right or wrong answers, just your honest perspectives."
Example Questions:
Describe a moment when you felt most fulfilled or happy. What was happening, and who was there?
Think of a time when you faced a difficult decision. How did you decide, and what criteria guided your choice?
Imagine you have a day to spend any way you wish, without any obligations. What would you choose to do, and why?
Expansion Phase User Prompt
"Now that we've started to understand what drives you, let's delve a little deeper into your values. This next set of questions will help us uncover more layers of what you find important."
Example Questions:
When you think about people you truly admire, what qualities do they possess that you value?
Reflect on a situation where you felt out of place or uncomfortable. What was missing or clashing with your values?
If you could change one aspect of society, what would it be and why?
Describe a book, movie, or story that deeply moved you. What about it resonated with you?
Follow-up and Dynamic Interactions
Adaptive Questions: Based on user responses, the form should generate follow-up questions that dig deeper or explore different aspects of the user's answers. For example, if a user mentions feeling fulfilled when helping others, a follow-up might explore what aspect of helping feels most rewarding.
Analysis and Summary: After the conversation, the system should analyze the responses to identify recurring themes, words, and sentiments that align with known values. Then, it should summarize these findings, presenting the user with their 3 core values and 4 adjacent values.

Prompt for Uncovering User Values Through Conversational AI
Objective: To engage users in a reflective and insightful conversation that naturally uncovers their 3 core values and 4 adjacent values, facilitating a journey of self-discovery and personal understanding.

Instructions for AI (acting as an empathetic and insightful psychologist):

Initiate Conversation with Warmth and Openness:
Start by creating a welcoming and safe space for conversation. Express genuine interest in understanding the user's perspective and experiences.
Example: "I'm here to explore with you what truly matters in your life. Let's embark on this journey together, with openness and curiosity."
Employ Active Listening and Reflective Techniques:
As the user shares their thoughts and experiences, use active listening to show understanding and encourage deeper exploration.
Reflect back what you've heard in a way that prompts further reflection and clarification.
Example: "It sounds like making a positive impact is something that deeply resonates with you. Can you share an experience where this value guided your actions?"
Use Adaptive Questioning Based on Psychological Frameworks:
Incorporate questions inspired by psychological theories and frameworks to guide the conversation towards uncovering values.
Adjust questions based on the user's responses, exploring different aspects of their experiences and reflections.
Example: "Considering a time when you felt your actions were most in alignment with your true self, what were you doing, and why was that moment significant?"
Explore Values through Hypothetical Scenarios and Real-life Situations:
Present hypothetical scenarios or ask about real-life situations that require the user to make decisions or reflect on their preferences and priorities.
Example: "Imagine you have the opportunity to lead a project with a significant impact. What cause would you choose to focus on, and why?"
Identify and Explore Value Conflicts:
When discrepancies or conflicts in values emerge, gently encourage the user to explore these conflicts to gain deeper insights.
Example: "You've mentioned both freedom and security as important to you. Can you recall a situation where you had to prioritize one over the other? What was that like?"
Summarize and Reflect Observed Values Back to the User:
Throughout the conversation, summarize key points and reflect observed values back to the user for confirmation or adjustment.
Example: "From our conversation, it seems that compassion, integrity, and growth stand out as significant values for you. How do these resonate with your sense of self?"
Facilitate a Reflective Closure:
Conclude the session by encouraging the user to reflect on the conversation and how it may have affirmed or expanded their understanding of their values.
Offer an open invitation for further reflection or discussion.
Example: "Our journey today has revealed some insightful reflections about what's truly important to you. How does this understanding resonate with your sense of who you are and aspire to be?"

Follow-Up Actions for AI:
Based on the conversation, dynamically generate a summary of the 3 core values and 4 adjacent values identified, providing brief explanations or examples from the user's responses.
Encourage the user to revisit these values periodically or when facing significant decisions, as values can evolve over time.

This structured approach ensures that the conversational AI, acting as an empathetic and insightful psychologist, can effectively guide users through a process of self-discovery to uncover and reflect on their core and adjacent values in a meaningful, accurate, and insightful manner. 
Connection to Self
Passport Quest Sections 
Values (V): By discussing stories or movies that moved you and qualities you admire in others, we pinpoint your core values.
Passion (PA): Questions about your most exciting days and activities you advocate for help identify your passions.
Interests (I): We explore what makes you feel engaged and alive, along with topics you're curious about, to uncover your latent and emerging interests.
Beliefs (B): We delve into your drawn beliefs and moments of significant personal change to understand your philosophical outlook.
Talents (T): Identifying tasks you excel at effortlessly and unexpected compliments helps highlight your natural talents.
Skills (S): Recalling problem-solving instances and moments of competence uncovers your skills.
Impact (IM): Reflections on proud contributions and desired changes in the world reveal where you want to make an impact.
Professional Purpose (PP) & Life Purpose (LP): Discussions about meaningful work, fulfilling career moments, and stories where you made a difference provide insight into your professional and life purposes.
Short-Term (STG) & Long-Term Goals (LTG): We ask about your ambitions for the next year and your ideal future to understand your goals.
Values (V)
Knowledge Base
These values reflect what individuals prioritize in their lives, guiding their decisions, behaviors, and interactions with others. Below is a list of potential values that can be identified in a person, categorized for clarity:

Personal Growth and Self-Improvement
Curiosity
Knowledge
Creativity
Self-discipline
Wisdom
Personal development
Resilience
Interpersonal Relations
Family
Friendship
Love
Empathy
Respect
Trust
Compassion
Work and Career
Achievement
Ambition
Professionalism
Hard work
Leadership
Teamwork
Innovation
Ethics and Morality
Honesty
Integrity
Fairness
Justice
Responsibility
Loyalty
Transparency
Lifestyle Preferences
Health and wellness
Adventure
Comfort
Simplicity
Luxury
Sustainability
Balance
Community and Society
Social justice
Equality
Diversity
Community service
Philanthropy
Environmentalism
Patriotism
Spirituality and Philosophy
Faith
Spirituality
Inner peace
Harmony
Enlightenment
Tradition
Freedom and Autonomy
Independence
Freedom
Self-expression
Privacy
Adventure
Flexibility
Enjoyment and Pleasure
Fun
Humor
Leisure
Artistic expression
Sensory pleasure
Excitement
Security and Stability
Safety
Security
Stability
Order
Predictability
Control
Achievement and Success
Success
Achievement
Recognition
Prestige
Power
Wealth
Intellectual and Cognitive
Intellectual growth
Critical thinking
Open-mindedness
Thoughtfulness
Insightfulness
Physical and Health
Physical fitness
Health
Vitality
Physical activity
Nutrition

This extensive list of values serves as a foundation for understanding the diverse priorities and guiding principles that individuals may hold. By incorporating these values into the knowledge base, the AI can be trained to more accurately identify and categorize users’ values based on their responses, leading to improved insights and compatibility assessments.
Core vs. Supporting Values 
To effectively categorize and distinguish between the primary and secondary values of an individual, clear and intuitive terminology will be essential. This helps users understand the distinction and ensures that the AI processes the information accurately. Here’s a suggested approach for wording and categorization:

Categorization:
Core Values: These are the foundational principles that are most important to an individual, guiding their major life decisions, behaviors, and how they prioritize their time and resources. Core values are deeply ingrained and are often non-negotiable when it comes to compatibility with others.
Supporting Values: These values are significant but play a more flexible role in an individual’s life. They influence daily choices and preferences and are important for overall satisfaction and well-being, but they may be more subject to change or negotiation than core values.

Implementation in the Questionnaire:
When asking participants to select or rank their values as part of the assessment, you could structure the instructions like this:

“Please identify and select your Core Values by choosing the three values that are most crucial to you. These should be the principles that you hold in the highest regard and that influence your major life decisions and relationships.

Next, select four Supporting Values that are also important to you but serve a more complementary role in shaping your daily life and interactions with others. These values, while significant, might be more adaptable or negotiable in relation to your core values.”
Justification for Terms:
Core vs. Supporting: The terms “core” and “supporting” naturally suggest a hierarchy where core values are foundational, akin to the pillars of a person’s value system, while supporting values add structure and detail, enriching the individual’s profile without bearing the entire weight of their decision-making process.
Flexibility and Negotiability: This distinction implicitly communicates to users and the AI alike that while core values are steadfast, supporting values have a degree of flexibility, which is crucial for understanding interpersonal dynamics and compatibility.

This approach allows for a nuanced understanding of individuals’ values, facilitating more accurate matches based on both fundamental compatibilities (core values) and the potential for growth and adaptation in relationships (supporting values).

For matching individuals based on values, recognizing both core and supporting values is crucial for ensuring deep compatibility as well as the potential for adaptable and enriching relationships. Here’s how the compatibility matching could be structured, taking into account the distinction between core and supporting values:
Compatibility Matching
For values-based compatibility, ensuring alignment on core values between individuals is crucial for establishing a foundation of mutual understanding and shared priorities, which are essential for long-term harmony and connection. Core values, being the most deeply held beliefs, guide significant life choices and interactions, making their alignment a cornerstone for compatibility. Supporting values, while also important, bring diversity and richness to relationships by allowing room for growth, exploration, and adaptability. For example, two individuals might share core values of honesty and compassion, ensuring a strong ethical and empathetic bond, but might have different supporting values such as preferences for adventure versus tranquility. This variation in supporting values can enrich the relationship, introducing each person to new experiences and ways of thinking, while their aligned core values maintain a deep, underlying connection. This nuanced approach to values-based compatibility fosters relationships that are both solidly grounded and dynamically enriching.
Sample Questions 
What story or movie deeply moved you, and what about it resonated with you the most?
Media that impacts us can reflect our core values; this question helps individuals connect with those values indirectly.
When you think about people you truly admire, what qualities do they have that you wish to see more of in the world?
Suggests an exploration of admired qualities in others as a mirror for the individual's own values.
Passion (PA)
Knowledge Base 



For identifying passions in a way that aligns with the distinction made between core and supporting values, a similar but slightly simplified approach could be effective. Given that passions often reflect what individuals are most enthusiastic about and what drives their engagement with activities, hobbies, and interests, distinguishing between a primary or “burning” passion and additional passions can help in understanding an individual’s priorities and potential compatibility with others. Here’s a suggested framework:

Categorization:
Primary Passion: This is the individual’s most profound passion, something they are deeply committed to and that significantly influences their life choices, how they spend their time, and often, their sense of purpose.
Secondary Passions: These are additional interests that the individual is enthusiastic about and enjoys pursuing. While important and fulfilling, they may not hold as central a role in the individual’s life as the primary passion.
Implementation in the Questionnaire:

When incorporating this into the assessment, you could frame the instructions as follows:

“Please identify your Primary Passion by selecting the one passion that stands out to you as your greatest source of joy, motivation, and engagement. This should be something that you feel deeply connected to and that significantly influences your daily life and long-term goals.

Next, select up to two Secondary Passions that you also enjoy and dedicate time to. These passions enrich your life and provide additional avenues for joy and fulfillment, but they may not define your life to the extent of your primary passion.”
Justification for Terms and Number:
Primary vs. Secondary: Keeping the terminology consistent with “core” and “supporting” values, “primary” and “secondary” passions intuitively denote a hierarchy. This helps to easily differentiate the passions that are most defining of an individual from those that are additional but still meaningful.
Limiting the Number: Focusing on identifying one primary passion and up to two secondary passions limits the scope to what is most relevant for compatibility matching, ensuring clarity without overwhelming detail. It reflects the practical reality that while many people have multiple interests, there are usually one or a few passions that are pursued more fervently.
Compatibility Matching 
For passion-based matching, prioritizing alignment on primary passions ensures individuals share fundamental enthusiasms, laying a strong foundation for compatibility. Secondary passions introduce diversity, enriching connections by offering opportunities to explore and share varied interests, thus broadening the relationship’s horizon and potential for growth.
Sample Questions
Can you recall a day when you felt really excited from the moment you woke up? What were you looking forward to doing?
This question is designed to indirectly identify activities that spark excitement and joy, hinting at underlying passions.
Is there a particular topic or activity that you find yourself defending or advocating for with friends or family?
Looks for subjects the individual feels strongly about, indicating areas of deep interest or passion.
Interests (I)
Knowledge Base
Arts and Culture
Visual arts (painting, sculpture, photography)
Performing arts (theater, dance, opera)
Cinematography (film making, watching movies)
Music (playing instruments, singing, composing)
Literature (reading, writing, poetry)
Crafts (pottery, jewelry making, textile arts)
Fashion design and creation
Culinary arts (cooking, baking, food decoration)
Outdoor and Adventure
Hiking, backpacking
Camping
Rock climbing, mountaineering
Water sports (surfing, kayaking, diving)
Skydiving, paragliding
Adventure racing
Wildlife and nature exploration
Gardening, landscaping
Sports and Fitness
Team sports (soccer, basketball, baseball)
Individual sports (tennis, golf, martial arts)
Fitness and gym activities
Yoga, Pilates
Running, cycling
Winter sports (skiing, snowboarding, ice skating)
Aquatic sports (swimming, water polo)
Science and Technology
Astronomy, astrophysics
Robotics, AI
Programming, software development
Electronics, DIY tech projects
Environmental science, sustainability
Biology, chemistry, physics
Space exploration, rocketry
Social Activities and Volunteering
Community service, volunteering
Social clubs, fraternities, sororities
Political activism, social justice causes
Board games, card games
Book clubs, discussion groups
Wine tasting, mixology
Learning and Education
Language learning
Historical studies, archaeology
Philosophy, theology
Online courses, MOOCs
DIY learning, skill development
Lectures, workshops, seminars
Crafts and DIY
Woodworking, carpentry
Metalworking, welding
Knitting, crocheting, embroidery
Scrapbooking, papercrafts
Home renovation, interior design
Model building, miniature painting
Gaming and Entertainment
Video games, eSports
Board games, tabletop RPGs
Puzzles, brain teasers
Magic, illusion
Comic books, graphic novels
Anime, manga
Travel and Exploration
Cultural exploration, anthropological trips
Eco-tourism, sustainable travel
Culinary tours, gastronomy
Historical site exploration
Luxury travel, cruises
Backpacking, budget travel
Wellness and Spirituality
Meditation, mindfulness
Spiritual practices, religious studies
Natural health, holistic wellness
Retreats, wellness tourism
Psychic practices, astrology
Hobbies and Miscellaneous
Collecting (coins, stamps, antiques)
Photography, videography
Pet care, breeding, training
Aquarium keeping
Bird watching
Homebrewing, winemaking
Capturing Snapshot, not Hierarchy 
When it comes to interests, which can range broadly and vary greatly from person to person, it’s practical to capture a snapshot of an individual’s preferences without creating too complex a hierarchy. Unlike core values or primary passions, interests often fluctuate and can be explored in various degrees of engagement. However, for compatibility purposes, identifying interests can help match individuals with shared or complementary activities and hobbies. Given this, a tiered approach might not be as necessary as with values and passions, but a categorization can still be beneficial for clarity and matching precision.
Categorization
Instead of distinguishing between primary and secondary interests, it might be more useful to categorize interests based on themes or domains. This allows for a broader understanding of an individual’s likes and how they might intersect with others, facilitating matches based on shared or mutually appreciable interests.
Implementation in the Questionnaire
“Please select your interests from the following categories. Choose as many as apply to you. This will help us match you with individuals who share similar interests or who might be complementary to your own.”
Flexibility and Exploration
Encouraging participants to select multiple interests across different categories reflects the multifaceted nature of individual preferences and the potential for growth and exploration in new areas. This approach acknowledges that interests can serve as both a foundation for shared activities and a gateway to exploring new experiences together.
Compatibility Matching
For matching purposes, the system can use these categories to identify overlaps and potential areas of mutual interest between individuals. Matching can prioritize shared categories but also consider complementary interests, fostering opportunities for roommates or community members to introduce each other to new experiences.
Sample Questions
Tell me about a moment or experience when you felt truly engaged and alive. What were you doing? (I)
Encourages reflection on past experiences to identify engaging activities.
What topics do you find yourself endlessly curious about, even if you haven't explored them deeply yet? (I)
Opens up the conversation for latent interests or emerging curiosities.
Beliefs (B)
Knowledge Base
Religious and Spiritual Beliefs
Monotheism (belief in one God)
Polytheism (belief in multiple gods)
Atheism (disbelief in gods)
Agnosticism (belief that the existence of gods is unknown or unknowable)
Pantheism (belief that the universe and god are identical)
Animism (belief that objects, places, and creatures all possess a spiritual essence)
Spiritual but not religious (individual spiritual practices without adherence to organized religion)
New Age and esoteric beliefs
Ethical and Moral Beliefs
Human rights and equality
Justice and fairness
Ethical treatment of animals
Environmental stewardship and sustainability
Non-violence and pacifism
Freedom of speech and expression
Ethical consumerism
Political and Societal Beliefs
Political ideologies (liberalism, conservatism, socialism, etc.)
Democracy and governance
Social welfare and security
Immigration and multiculturalism
Education and healthcare policies
Law enforcement and criminal justice
Gender equality and LGBTQ+ rights
Philosophical Beliefs
Existentialism (concern with existence, especially human existence as viewed by the individual)
Rationalism (emphasis on reasoning as a source of knowledge)
Empiricism (emphasis on observational evidence via sensory experience as the source of knowledge)
Nihilism (belief that life is without objective meaning, purpose, or intrinsic value)
Stoicism (philosophy of personal ethics informed by its system of logic and views on the natural world)
Economic Beliefs
Free market capitalism
Social market economy
Planned economy
Universal basic income
Wealth distribution and taxation
Consumerism vs. minimalism
Lifestyle Beliefs
Veganism and vegetarianism
Zero waste and minimalism
Holistic and alternative medicine
Work-life balance
Family and parenting philosophies
Digital minimalism and technology use
Interpersonal and Social Beliefs
Community and collectivism vs. individualism
Traditional vs. modern family structures
Importance of friendship and social networks
Views on marriage and partnerships
Communication and conflict resolution styles
Educational and Knowledge Beliefs
Importance of formal education vs. self-learning
Science and technology perspectives
Historical revisionism vs. traditionalism
Beliefs about media and information
Health and Wellness Beliefs
Medical intervention vs. natural healing
Mental health and psychological well-being
Physical fitness and body image
Dietary habits and nutrition beliefs
Fundamental vs. Secondary Beliefs 
For understanding and categorizing beliefs in a way that enhances compatibility matching, a nuanced approach is necessary to capture the complexity of individual convictions. Unlike passions and interests, beliefs often constitute the core principles that guide a person’s understanding of the world and their place within it. Given this, it’s valuable to identify not just the beliefs themselves but the intensity and prioritization of these beliefs in a person’s life. Here’s a suggested framework:
Categorization
Fundamental Beliefs: These are deeply held beliefs that significantly shape an individual’s worldview, decision-making, and lifestyle. They are often non-negotiable and play a central role in defining a person’s identity and actions.
Secondary Beliefs: These beliefs are also important to the individual but might be more subject to change or reevaluation. They influence daily decisions and perspectives but do not hold as much weight as fundamental beliefs in shaping the individual’s core identity.
Implementation in the Questionnaire
When integrating this into the assessment, the instructions could be as follows:

“Please identify your Fundamental Beliefs by selecting those that are most critical to you. These should be the convictions that deeply influence how you view the world and guide your major life choices. Consider beliefs that you hold to be central to your identity and that you would be unlikely to change.

Next, select your Secondary Beliefs that you also hold to be important. While these play a role in shaping your daily life and interactions, they may be more flexible or open to evolution over time compared to your fundamental beliefs.”
Justification for Terms and Number
Fundamental vs. Secondary: The terms “fundamental” and “secondary” clearly indicate a hierarchy, aligning with the approach used for “core” and “supporting” values and “primary” and “secondary” passions. This distinction helps participants and the matching algorithm understand which beliefs are most integral to a person’s identity versus those that are still significant but less central.
Scope of Identification: Identifying a set number of fundamental and secondary beliefs (e.g., three fundamental beliefs and up to four secondary beliefs) keeps the focus on what truly matters to the individual without diluting the impact of the most critical convictions. This approach acknowledges the depth and breadth of beliefs that people can hold while ensuring the matching process remains manageable and meaningful.
Compatibility Matching
For compatibility purposes, aligning individuals based on their fundamental beliefs can significantly enhance the likelihood of deep and lasting connections, as these beliefs are pivotal to their worldview and lifestyle. Secondary beliefs offer additional layers of compatibility, allowing for diversity and growth in relationships by bringing together individuals who share core convictions but may have different perspectives on less central issues.
Sample Questions
Are there any beliefs or philosophies you find yourself drawn to, even if you're not sure why?
Opens the conversation about beliefs in a way that allows for uncertainty and exploration, recognizing that beliefs can be a complex area for many.
Have you ever changed your mind about something important because of a conversation or something you learned? What was it about?
This question looks at flexibility and growth in beliefs, highlighting moments of significant personal change that might reveal core beliefs and how they influence decision-making.
Talents (T)
Knowledge Base
Intellectual Talents
Analytical thinking
Problem-solving
Logical reasoning
Mathematical aptitude
Linguistic skills (multilingualism, language learning)
Memory retention (eidetic memory, excellent recall)
Creative and divergent thinking
Academic excellence in specific subjects (e.g., history, science, literature)
Creative Talents
Artistic abilities (drawing, painting, sculpting)
Musical talents (instrumental skills, vocal performance, composition)
Writing (fiction, non-fiction, poetry, screenwriting)
Dance (choreography, performance)
Photography and videography
Design (graphic, fashion, interior, web)
Culinary arts (cooking, baking, food styling)
Acting and theatrical performance
Physical Talents
Athleticism (strength, endurance, agility)
Specific sports skills (soccer, basketball, swimming, etc.)
Physical coordination and balance
Flexibility and body control (gymnastics, yoga)
Manual dexterity (precision in hand-eye coordination tasks)
Endurance sports prowess (marathon running, cycling)
Extreme sports capabilities (rock climbing, surfing)
Interpersonal and Social Talents
Empathy and emotional intelligence
Public speaking and oratory
Leadership and team management
Negotiation and persuasion
Teaching and coaching abilities
Social perceptiveness
Conflict resolution
Networking and relationship building
Practical and Technical Talents
Mechanical skills (repair, construction, engineering)
Technological aptitude (software development, cybersecurity)
Artisanal crafts (woodworking, metalworking, textiles)
Gardening and horticulture
Animal training and care
Culinary techniques and innovation
Financial literacy and investment strategy
Organization and space optimization
Innovative and Entrepreneurial Talents
Innovation and invention
Strategic thinking and planning
Entrepreneurial startup success
Risk management and assessment
Market analysis and business intuition
Product development and marketing
Fundraising and capital growth
Scaling businesses and operations
Expressive and Performance Talents
Storytelling and narration
Stand-up comedy and humor
Magic and illusion
Voice acting and voiceover work
Puppetry and ventriloquism
Broadcasting (radio, podcasting)
Hosting and emceeing events
Miscellaneous Talents
Speed reading and efficient learning
Puzzle-solving (crosswords, Rubik’s cube)
Memory competitions and mnemonic techniques
Survival skills and bushcraft
Brewing (beer, wine, spirits)
Historical reenactment and knowledge
Collecting and curating

For talents, which encapsulate an individual’s natural aptitudes and developed skills, a clear categorization can enhance self-awareness and facilitate better compatibility matching, especially in environments where collaboration and complementary skill sets are valued. Here’s a structured approach tailored to identifying and categorizing talents:
Categorization
Primary Talents: These are an individual’s strongest talents, the skills or abilities where they excel and which often define significant aspects of their personal or professional identity. Primary talents are those an individual is most known for and are likely to be the basis of their contributions to a group or project.
Complementary Talents: While not as predominant as primary talents, these are additional skills or abilities an individual possesses. Complementary talents can enhance a person’s primary talents or contribute diversity to their skill set, offering breadth and versatility.
Implementation in the Questionnaire
“Please identify and select your Primary Talents by choosing the talent or talents that you excel in and are most passionate about. These should be abilities you’re not only good at but also enjoy and often serve as a key part of your identity or professional life.

Next, select up to three Complementary Talents that you also possess. While these might not be as prominent as your primary talents, they add depth to your abilities and can provide additional pathways for contribution, enjoyment, or both.”
Justification for Terms
Primary vs. Complementary: This distinction helps individuals prioritize their talents, focusing on their strongest areas while also acknowledging the range of their abilities. It mirrors the “core” vs. “supporting” framework used for values, providing a consistent approach to categorization across different aspects of the personality and skill assessment.
Depth and Breadth: Highlighting both primary and complementary talents allows for a balance between depth and breadth in understanding an individual’s capabilities. This is crucial for matching, as it enables the identification of both primary areas of strength and secondary skills that can enrich collaborations or community life.
Compatibility Matching
For compatibility purposes, matching individuals based on their primary talents ensures that each person can contribute their strongest skills to a communal or collaborative setting, fostering excellence and satisfaction. Complementary talents come into play by offering additional dimensions for compatibility, allowing for more nuanced and multifaceted team dynamics. For instance, in a project team, while one’s primary talent in analytical thinking might drive problem-solving, their complementary talent in communication could enhance team coordination and idea sharing.
Sample Questions
What are some things you do effortlessly that others seem to struggle with? (T)
Helps identify natural strengths or talents.
Is there a skill or ability you've been complimented on that surprised you? Why? (T)
Opens the door to recognizing unrecognized talents.
Skills (S)
Think about a time you helped someone with a problem. What did you do, and how did you figure it out?
By recalling a situation where they were naturally able to solve a problem, the individual may reveal hidden skills or innate abilities.
Have you ever been so absorbed in a task that you felt like an expert, even if you were just learning or doing it for fun? What was it?
Encourages individuals to think about moments of flow and competence, potentially uncovering skills they haven't formally recognized.
Impact (IM)
Knowledge Base 
Sample Questions
Can you share a time when you felt really proud of something you did for someone else or your community? What was the situation?
This question allows individuals to reflect on their actions' effects without requiring them to label these actions as impactful upfront.
If you could solve one problem in your community or the world, no matter how big or small, what would it be and why?
Encourages individuals to dream big or small about changes they wish to see, revealing areas where they feel motivated to make an impact.
Professional Purpose (PP)
Knowledge Base
Sample Questions 
When you think about work that feels meaningful, what comes to mind? (PP)
Aims to uncover innate senses of professional fulfillment without requiring a defined purpose.
Have there been moments in your career or studies when you felt particularly proud or fulfilled? What were you doing? (PP)
Seeks specific instances that might hint at deeper professional motivations.
Life Purpose (LP)
Knowledge Base
Sample Questions
Can you share a story where you felt you made a real difference in someone’s life or in a community? How did it make you feel? (LP)
Provides insight into actions and impacts that resonate on a personal level, potentially illuminating elements of life purpose.
When you imagine a world you want to live in, what does it look like? How do you see yourself contributing to it? (LP)
Encourages envisioning a broader contribution, hinting at underlying life purposes.

Short-Term Goals (STG)
Knowledge Base
Sample Questions
What is one thing you’d like to achieve or complete in the next year? (STG)
Identifies immediate ambitions or objectives.
Looking at the coming months, what steps do you feel drawn to take towards your interests or goals? (STG)
Encourages practical thinking about near-future actions.

Long-Term Goals (LTG)
Knowledge Base
Sample Questions
Imagine your ideal future in ten years. What are you most excited about? (LTG)
Facilitates dreaming about the future, allowing for a broad vision to emerge.
What legacy do you hope to leave behind? How does that reflect your values or dreams? (LTG)
Connects long-term aspirations with personal values and dreams.
Connection to Place 

Connection to People 
Psychological Compatibility: This includes compatibility in personality, conflict resolution styles, communication preferences, stress management, and empathy.
Aspirational Alignment & Goal Synergy: Aligning individual and shared aspirations and exploring collaborative efforts towards common goals.
Lifestyle and Habits: We look at daily routines, cleanliness, social habits, health practices, and hobbies.
Values and Beliefs: Fundamental values, cultural diversity, religious practices, and political views are considered to ensure harmony.
Environmental and Practical Considerations: Financial habits, space sharing, noise tolerance, pet preferences, and sustainability practices are reviewed.
Work and Productivity: Work habits, workspace needs, and productivity practices are matched for compatibility.
Learning and Development: Learning styles, educational goals, and personal growth activities are aligned.
Cultural Dimensions: Preferences in individualism vs. collectivism, power distance, uncertainty avoidance, and other cultural dimensions are considered to foster a supportive environment.
Psychological Compatibility
Personality Match: Alignment in the Big Five personality traits—Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism.
Conflict Resolution Styles: Approaches to resolving disagreements, emphasizing avoidance, accommodation, competition, compromise, or collaboration.
Communication Preferences: Preferred methods and frequency of communication, distinguishing between verbal vs. non-verbal and direct vs. indirect communication.
Stress Management: Strategies for coping with stress and maintaining emotional stability under pressure.
Empathy and Emotional Intelligence: Ability to empathize and respond to others' emotions, creating a supportive environment.
Short and Long Term Goals
Aspirational Alignment: Identifies and aligns individual and shared aspirations, highlighting short-term objectives (such as skill acquisition, financial milestones, or health and wellness targets) and long-term ambitions (career progression, educational achievements, or life milestones).
Goal Synergy: Explores the potential for collaborative efforts towards common goals or how individual goals can complement and support each other within the shared living arrangement.
Navigating Goal Differences: Offers strategies for respecting and accommodating differing goals, ensuring that personal ambitions enhance rather than hinder the shared living experience.
Lifestyle and Habits
Daily Routines and Schedules: Compatibility in daily life rhythms, including sleep, work, and leisure activities.
Cleanliness and Organization: Agreement on cleanliness standards and organizational habits.
Social Habits: Preferences for social interaction, hosting, and engagement in communal activities vs. solitude.
Health and Wellness Practices: Shared or respected health routines, including dietary habits, exercise, and mental health practices.
Hobbies and Interests: Common or mutually respected hobbies, fostering shared experiences and understanding.
Values and Beliefs
Core Values and Ethics: Alignment in fundamental values, ethics, and life aspirations.
Cultural and Background Diversity: Compatibility and respect for cultural diversity, encouraging mutual learning and adaptation.
Religious and Spiritual Beliefs: Mutual respect for religious and spiritual practices, or shared beliefs enhancing compatibility.
Political and Social Views: Alignment or respectful acceptance of political and social perspectives, facilitating harmonious coexistence.
Environmental and Practical Considerations
Financial Habits and Responsibilities: Agreement on financial contributions, budgeting, and management of shared expenses.
Space Sharing Preferences: Expectations about the use and division of shared and private spaces.
Noise and Privacy Tolerance: Compatibility in noise preferences and respect for individual privacy needs.
Pet Preferences and Allergies: Considerations for pet ownership, allergies, and comfort with animals.
Sustainability and Environmental Practices: Shared commitment to sustainability and eco-friendly living practices.
Resource Sharing Preferences: Preferences and expectations regarding the sharing of resources, such as food, appliances, and utilities.
Work and Productivity
Work Habits and Schedules: Compatibility in work schedules, including remote work needs and office hours.
Workspace Requirements: Preferences and expectations for dedicated workspaces, noise levels, and work-from-home setups.
Productivity Practices: Shared or respected productivity methods, work styles, and breaks.
Learning and Development
Learning Styles and Preferences: Compatibility in learning habits, including quiet study times, discussion-based learning, and multimedia use.
Educational Goals and Pursuits: Support for each other’s educational objectives, courses, and study schedules.
Personal Growth and Skill Development: Shared interests or support for skill development, hobbies, and personal growth activities.
Cultural Dimensions
Individualism vs. Collectivism: Preferences for individual autonomy versus a collective, group-based approach to living and decision-making.
Power Distance: Comfort with hierarchical relationships and authority within the living environment.
Uncertainty Avoidance: Tolerance for ambiguity and unpredictability in living arrangements and daily routines.
Masculinity vs. Femininity: Preferences for traditionally masculine values (e.g., competitiveness) versus feminine values (e.g., care and cooperation).
Long-Term vs. Short-Term Orientation: Alignment in focusing on long-term goals and traditions versus prioritizing immediate benefits and flexibility.
Indulgence vs. Restraint: Compatibility in the tendency towards gratification of desires and leisurely activities versus a more restrained, controlled approach to pleasures. 
Sample Questions: 
Psychological Compatibility
How do you typically approach conflicts with friends or family, and what strategies do you find most effective for resolving them?
Aims to understand the individual's conflict resolution style, whether they prefer addressing issues directly or seeking compromise.
Describe a time when you had to work closely with someone very different from you. How did you communicate and collaborate effectively?
Seeks insights into communication preferences and adaptability in diverse interpersonal dynamics.
Think about a stressful situation you've faced recently. How did you manage your stress, and what did you learn about yourself?
Explores stress management techniques and personal resilience, offering a glimpse into emotional coping strategies.
Can you share an example of when you felt deeply understood by someone? What made that interaction meaningful for you?
Investigates empathy and emotional intelligence, highlighting the capacity to connect and empathize with others.

Aspirational Alignment & Goal Synergy
What's a personal goal you're currently working towards, and how do you plan to achieve it?
Identifies short-term objectives and the practical steps envisioned to attain them, shedding light on planning and ambition.
Looking ahead, where do you see yourself in 10 years, and what values or dreams are guiding this vision?
Facilitates discussion on long-term ambitions and the underlying motivations, offering a perspective on future aspirations and values.

Lifestyle and Habits
Describe your ideal day from morning to night. What activities or routines are most important to you?
Provides insight into daily routines, lifestyle preferences, and prioritization of activities for well-being and satisfaction.
How do you define a clean and organized living space, and how do you maintain it?
Explores cleanliness and organization standards, reflecting personal habits and preferences in shared environments.

Environmental and Practical Considerations
How do you approach budgeting and managing expenses for shared resources or activities?
Inquires about financial habits and responsibility-sharing in communal settings, highlighting approaches to budgeting and expense management.
In a shared living or working space, how do you balance your need for privacy with community interaction?
Examines noise and privacy tolerance as well as space-sharing preferences, critical for harmonious co-living or co-working arrangements.

Learning & Development
When you're learning something new, what approach or method do you find most effective for you?
Aims to uncover individual learning styles and preferences, providing insight into how they absorb and process information most efficiently.
Can you share an experience where you learned a skill outside of a formal setting? What motivated you and how did you go about it?
Seeks to understand self-directed learning experiences, highlighting motivation for skill acquisition and personal growth outside traditional educational environments.
Reflecting on your educational or career journey, can you identify a moment of significant personal growth? What sparked it?
Investigates moments that have contributed to significant personal development, focusing on the catalysts for growth and the impact on their trajectory.
Imagine you could master a new skill or subject in the next year. What would it be, and why does it interest you?
Encourages members to envision future learning goals, shedding light on aspirations for skill development and areas of keen interest.
Connection to Nature 
Concerns : 
How do we make sure the user inputs accurate data ? 
How do we get them to Involve other people to talk about them
How do we get people to give us more information/spend more time answering questions? 
How do we continue to gather information on a recurring basis? 



"""