from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import JSONResponse

from app.api.v1.words.sort.schemas.input import SortWordsRequest
from app.services.domain.sort_word_service import SortWordService

router = APIRouter()


@router.post(
    path="/words/sort", response_class=JSONResponse, status_code=status.HTTP_200_OK
)
def sort_words(payload: SortWordsRequest) -> JSONResponse:
    """ """
    service = SortWordService()
    response = service.sort_words(payload)
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
