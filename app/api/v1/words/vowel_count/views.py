import logging

from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import JSONResponse

from app.api.v1.words.vowel_count.exceptions import VowelCountException
from app.api.v1.words.vowel_count.schemas.input import VowelCountRequest
from app.default_exceptions.exceptions import InternalServerErrorException
from app.services.domain.vowel_count_service import VowelCountService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    path="/words/vowel-count",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
)
def vowel_count(payload: VowelCountRequest) -> JSONResponse:
    """ """
    service = VowelCountService()
    try:
        response = service.return_total_vowels(payload.words)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)
    except VowelCountException as error:
        raise error
    except Exception as error:
        logger.error("Unmapped error", extra={"error": error})
        raise InternalServerErrorException()
