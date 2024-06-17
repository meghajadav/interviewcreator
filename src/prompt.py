prompt_template = ("""
    You are an expert in finding entities based on documentation.
    Your goal is to discover all entities from the document.
    you do this by asking the question about the text below:

    -------------------------
    {text}
    -------------------------
    Create graphs that will show the relationship between the entity.
    Make sure not to lose any important information.

    Questions:

    """)


refine_template =  ("""
    You are an expert at creating practice questions based on material and documentation.
    Your goal is to help a person by providing all possible questions for a test. 
    We have received some questions {existing_answer}.
    We have the option to refine the existing questions or add new questions.
    Only if necessary with some more context below.
    --------------------
    {text}
    --------------------
    Given the new context, refine the original questions in english.
    If the context is not helpful, please provide the original question.
    QUESTIONS:                                        
    """)