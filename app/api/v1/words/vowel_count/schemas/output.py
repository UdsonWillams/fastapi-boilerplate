# Inserir modelos de output, responses.
from pydantic import BaseModel


class VowelCountResponse(BaseModel):
    response: dict
