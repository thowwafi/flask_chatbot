from llama_index import SimpleDirectoryReader, GPTListIndex, LLMPredictor, PromptHelper, GPTVectorStoreIndex, ServiceContext, StorageContext
from llama_index import load_index_from_storage
from langchain import OpenAI
import sys
import os


def loadVectorIndex(path):
    storage_context = StorageContext.from_defaults(persist_dir=path)
    vectorIndex = load_index_from_storage(storage_context=storage_context)

    return vectorIndex
