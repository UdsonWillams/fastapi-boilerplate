from fastapi import APIRouter

from app.api.v1.currency_converter.views import router as currency_converter_router
from app.api.v1.words.sort.views import router as sort_words_router
from app.api.v1.words.vowel_count.views import router as vowel_count_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(currency_converter_router, tags=["Currency Converter"])
v1_router.include_router(sort_words_router, tags=["Sort Words"])
v1_router.include_router(vowel_count_router, tags=["Vowel Count"])
