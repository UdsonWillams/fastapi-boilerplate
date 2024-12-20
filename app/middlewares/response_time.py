import logging
from time import time

from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)


class ResponseTimeMiddleware(BaseHTTPMiddleware):
    """
    A ideia desse middleware é de retornar o valor de tempo de
    resposta dos endpoints chamados.
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        initial_time = time()
        response = await call_next(request)
        final_time = time() - initial_time
        elapsed_time = round(final_time, 3)
        response.headers.update({"X-Response-Time": elapsed_time})
        return response
