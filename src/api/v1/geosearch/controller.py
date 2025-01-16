from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.geosearch.schema import FindStreetSchema
from core.database import db_conn
from service.finder import FinderService


router = APIRouter()


@router.post("/street/find/")
async def find_street(
    data: FindStreetSchema,
    session: Annotated[AsyncSession, Depends(db_conn.get_db)],
):
    finder_service = FinderService(session=session)
    async with session.begin():
        highways = await finder_service.find_street(street=data.street)
    return highways
