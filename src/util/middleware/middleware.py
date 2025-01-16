from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from core.config import config as cfg


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=cfg.cors.allowed_hosts,
        allow_credentials=cfg.cors.allowed_credentials,
        allow_methods=cfg.cors.allowed_methods,
        allow_headers=cfg.cors.allowed_headers,
    ),
]
