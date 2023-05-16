from llama_index import SimpleDirectoryReader, GPTListIndex, LLMPredictor, PromptHelper, GPTVectorStoreIndex, ServiceContext, StorageContext
from llama_index import load_index_from_storage
from langchain import OpenAI
import sys
import os
from decouple import config


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
model_name = config("MODEL_NAME")

def createVectorIndex(path):
    max_input = 4096
    tokens = 200
    chuck_size = 600
    max_chunk_overlap = 20

    prompt_helper = PromptHelper(max_input, tokens, chuck_size, max_chunk_overlap, chunk_size_limit=chuck_size)
    llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name=model_name, max_tokens=tokens))

    docs = SimpleDirectoryReader(path).load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=llmPredictor, prompt_helper=prompt_helper)

    vectorIndex = GPTVectorStoreIndex.from_documents(docs, service_context=service_context)
    vectorIndex.storage_context.persist(persist_dir="Store")

    return vectorIndex


def loadVectorIndex(path):
    storage_context = StorageContext.from_defaults(persist_dir="Store")
    vectorIndex = load_index_from_storage(storage_context=storage_context)

    return vectorIndex


if __name__ == "__main__":
    path = sys.argv[1]
    print("Creating Vector Index")
    vectorIndex = createVectorIndex(path)
    print("Vector Index Created")
