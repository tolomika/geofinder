from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from model.line import PlanetOsmLine


class FinderService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_street(self, street: str) -> list[str]:
        """
        Выполняет полнотекстовый поиск по столбцу `name` и возвращает список значений.
        :param street: Название улицы
        :return: словарь с `name`
        """
        stmt = select(PlanetOsmLine.name).where(
            func.similarity(PlanetOsmLine.name, street) >= 0.3
        )
        result = await self.session.scalars(stmt)
        return result.all()
