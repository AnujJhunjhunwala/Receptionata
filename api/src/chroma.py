import chromadb
import langchain_chroma
from langchain_openai import OpenAIEmbeddings
from pydantic_settings import BaseSettings


class ChromaConfig(BaseSettings):
    chroma_hostname: str
    chroma_port: int


def get_chroma_client() -> langchain_chroma.Chroma:
    """
    :return: ChromaDB client with configuration obtained from
    the environment and an OpenAI embeddings function.
    """

    # gets config from env vars
    config = ChromaConfig()  # type: ignore

    return langchain_chroma.Chroma(
        client=chromadb.HttpClient(host=config.chroma_hostname, port=config.chroma_port),
        collection_name="documents",
        embedding_function=OpenAIEmbeddings(),
    )
