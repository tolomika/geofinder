from fastapi import APIRouter

from api.v1.api_v1 import general_router_v1 as v1


general_router = APIRouter(prefix="/api")

general_router.include_router(v1)
