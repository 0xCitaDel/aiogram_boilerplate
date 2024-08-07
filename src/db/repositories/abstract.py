import abc
from typing import Generic, TypeVar
from collections.abc import Sequence

from sqlalchemy import ScalarResult, delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Base


Model = TypeVar('Model', bound=Base)


class AbstractRepository(Generic[Model]):

    def __init__(self, model: type[Model], session: AsyncSession):
        self.model = model
        self.session = session

    async def add(self, data: list):
        stmt = insert(self.model).values(data).returning(self.model.id)
        await self.session.scalars(stmt)

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(data).returning(self.model.id)
        return await self.session.scalar(stmt)

    async def get(self, ident: int | str) -> Model:
        return await self.session.get(entity=self.model, ident=ident)

    async def get_by_where(self, whereclause) -> ScalarResult[Model]:
        statement = select(self.model).where(whereclause)
        res = (await self.session.scalars(statement))
        return res

    async def get_many(
        self, whereclause, limit: int = 100, order_by=None
    ) -> Sequence[Base]:
        statement = select(self.model).where(whereclause).limit(limit)
        if order_by:
            statement = statement.order_by(order_by)

        return (await self.session.scalars(statement)).all()

    async def get_all(self) -> Sequence[Base]:
        query = select(self.model)
        result = await self.session.scalars(query)
        return result.all()

    async def delete(self, whereclause) -> None:
        statement = delete(self.model).where(whereclause)
        await self.session.execute(statement)

    @abc.abstractmethod
    async def new(self, *args, **kwargs) -> None:
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        return instance
