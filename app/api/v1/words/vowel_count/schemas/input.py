# Inserir modelos de input, requests.
from pydantic import BaseModel


class VowelCountRequest(BaseModel):
    words: list[str]
