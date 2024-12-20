from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import (
    JSONResponse,
    RedirectResponse,
)

router = APIRouter(tags=["Health Checker"])


@router.get(
    path="/health",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
)
def check_health() -> JSONResponse:
    return JSONResponse(content={"status": "OK"})


@router.get(
    path="/db_health",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
)
def check_db_health():
    return True
    # try:
    #     with get_engine().connect():
    #         return True
    # except OperationalError:
    #     return False


@router.get("/", include_in_schema=False)
def return_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")
