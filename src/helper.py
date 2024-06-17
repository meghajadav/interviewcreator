from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from src.prompt import *
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_API_KEY=os.getenv("open_ai_api_key")

os.environ["OPENAI_API_KEY"]=OPEN_AI_API_KEY

def process_file(file_path):

    """
    load the pdf file on the given file path and read the page content 
    of the file. Then it will perform chunking using TokenTextSplitter which 
    takes model gpt-3.5-turbo as an input to do chunking along with chunk_size
    and chunk_overlap as input parameters.

    input= file path
    output= chunked document 

    We are chunking the document twice in this first we chunk with the bigger 
    chunk size that is 10000 and then with smaller chunk size that is 1000.

    As it is proved this way we get better performance. 
    """    
    loader = PyPDFLoader(file_path)
    data = loader.load()
    question_gen = ''

    for page in data:
        question_gen+=page.page_content

    text_splitter = TokenTextSplitter(
    model_name = 'gpt-3.5-turbo',
    chunk_size = 10000, 
    chunk_overlap = 200
    )
    chunk_question =text_splitter.split_text(question_gen)

    document_question_gen = [Document(page_content=text) for text in chunk_question ]
    text_splitter_2 = TokenTextSplitter(
    model_name = 'gpt-3.5-turbo',
    chunk_size = 1000, 
    chunk_overlap = 100
    )

    doc_ques_gen =text_splitter_2.split_documents(document_question_gen)

    return document_question_gen, doc_ques_gen

def llm_pipeline(file_path):
    document_question_gen, doc_ques_gen = process_file(file_path)

    llm_gen_ques_pipeline = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.3
    )

    
    
    prompt_ent = PromptTemplate(template=prompt_template, input_variables=['text'])

    

    refine_prompt_ques_template = PromptTemplate(
    input_variables=['existing_answer', 'text'],
    template=refine_template
    )


    ques_gen_chain =  load_summarize_chain(llm = llm_gen_ques_pipeline,
                                       chain_type='refine',
                                       verbose=True,
                                       question_prompt=prompt_ent,
                                       refine_prompt = refine_prompt_ques_template)


    ques = ques_gen_chain.run(doc_ques_gen)

    embeddings = OpenAIEmbeddings()

    vectore_store = FAISS.from_documents(document_question_gen, embeddings)

    llm_ans_gen = ChatOpenAI(temperature=0.1, model='gpt-3.5-turbo')
    lst_ques = ques.split('\n')

    filtered_ques_lst = [ele for ele in lst_ques if ele.endswith('?') or ele.endswith('.')]

    llm_ans_gen=RetrievalQA.from_chain_type(llm=llm_ans_gen,
                            chain_type='stuff',
                            retriever=vectore_store.as_retriever())
    return llm_ans_gen, filtered_ques_lst

# for que in lst_ques:
#     print("Question::", que)
#     answer = llm_ans_gen.run(que)
#     print('Answer::', answer)
#     print('--------------------------------\\n\\n')
#     with open('answer.txt', 'a') as f:
#         f.write('Question: '+que+'\\n')
#         f.write('Answer: '+answer+'\\n')
#         f.write('--------------------------------\\n\\n')





