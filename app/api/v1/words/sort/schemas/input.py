# Inserir modelos de input, requests.
from pydantic import BaseModel


class SortWordsRequest(BaseModel):
    words: list[str]
    order: str
