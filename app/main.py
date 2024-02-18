from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers.calculate_route import router


app = FastAPI()


app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ALLOW_ORIGINS],
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=[settings.ALLOW_METHODS],
    allow_headers=[settings.ALLOW_HEADERS],
)
