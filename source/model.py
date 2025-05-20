from openai import OpenAI
from langchain.document_loaders import PyMuPDFLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import ElasticsearchStore
from elasticsearch import Elasticsearch

import os
from glob import glob

def call_llm(prompt: str, system_prompt: str, rag_information: str, history: list, model: str="gpt-4o-mini"):
    client = OpenAI()
    response = client.chat.completions.create(  
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def call_rag(query: str, es_cloud_id: str, es_username: str, es_password: str, index: str):
    es_connection = Elasticsearch(
    cloud_id=es_cloud_id,
    basic_auth=(es_username, es_password),
    )

    elasticsearch_store = ElasticsearchStore(
        embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
        index_name=index,
        es_connection=es_connection,
    )
    results = elasticsearch_store.similarity_search(query, k=3)
    return results.__str__()



def call_agent(
    query: str,
    system_prompt: str,
    his_messages: list,
    es_cloud_id: str,
    es_username: str,
    es_password: str,
    index: str,
):
    # Call the RAG function to get the relevant information
    rag_information = call_rag(query, es_cloud_id, es_username, es_password, index)

    # Call the LLM function with the query and the relevant information
    response = call_llm(query, system_prompt, rag_information, his_messages)
    return response


    



