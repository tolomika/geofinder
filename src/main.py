from fastapi import FastAPI

from api.api import general_router
from core.config import config as conf
from util.exception_handlers.exception_handlers import exception_handlers
from util.middleware.middleware import middleware


app = FastAPI(
    docs_url="/swagger/" if conf.app.debug else None,
    redoc_url="/redoc/" if conf.app.debug else None,
    middleware=middleware,
    exception_handlers=exception_handlers,
)
app.include_router(general_router)
