from fastapi import APIRouter

from api.v1.geosearch.controller import router as geosearch


general_router_v1 = APIRouter()
general_router_v1.include_router(geosearch, prefix="/v1")
