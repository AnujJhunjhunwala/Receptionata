from typing import List, Dict, Any

from fastapi import APIRouter, Depends
from langchain_chroma import Chroma
from pydantic import BaseModel

from chroma import get_chroma_client


receptionata_router = APIRouter()


class QueryRequestBody(BaseModel):
    query: str


@receptionata_router.post("/relevant-chunks")
async def answer_query(
    body: QueryRequestBody,
    chroma_client: Chroma = Depends(get_chroma_client)
) -> List[Dict[str, Any]]:
    return [doc.dict() for doc in chroma_client.similarity_search(query=body.query)]
