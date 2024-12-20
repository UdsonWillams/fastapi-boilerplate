# Inserir modelos de output, responses.
from pydantic import BaseModel


class SortWordsResponse(BaseModel):
    response: list
