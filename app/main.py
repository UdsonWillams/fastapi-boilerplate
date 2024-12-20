import logging
from logging import config

from fastapi import FastAPI

from app import lifespan
from app.api import api_router
from app.core.logger import logger_config
from app.core.settings import get_settings

config.dictConfig(logger_config)
logger = logging.getLogger("app")

settings = get_settings()

app = FastAPI(
    title="FastApi Boilerplate",
    description="Api para servir de base para novos projetos",
    docs_url="/swagger",
    redoc_url="/docs",
    separate_input_output_schemas=True,
    lifespan=lifespan,
)
app.include_router(router=api_router)
