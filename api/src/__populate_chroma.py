import pathlib

import bs4
from dotenv import load_dotenv
from langchain_community.document_loaders.html_bs import BSHTMLLoader
from langchain_community.document_loaders.pdf import PDFMinerLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from chroma import get_chroma_client


if __name__ == "__main__":
    load_dotenv()

    DATA_DIR = pathlib.Path(__file__).parent / "data"

    # text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    #     model_name="gpt-3.5-turbo",
    #     chunk_size=1000,
    #     chunk_overlap=200,
    # )
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
    )

    documents = []
    for pdf in map(str, DATA_DIR.glob("*.pdf")):
        documents.extend(PDFMinerLoader(pdf).load())
    for html in DATA_DIR.glob("*.html"):
        loader = BSHTMLLoader(
            html,
            bs_kwargs=dict(
                features="html.parser",
                parse_only=bs4.SoupStrainer("article"),
            ),
        )
        documents.extend(loader.load())

    documents = text_splitter.split_documents(documents)

    chroma = get_chroma_client()
    chroma.add_documents(documents)
