from typing import Any, Awaitable, Callable, Union

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.structures.data_structure import TransferData
from db.database import Database



class DatabaseMiddleware(BaseMiddleware):
    """This middleware throw a Database class to handler."""

    async def __call__(
        self,
        handler: Callable[[Union[Message, CallbackQuery], TransferData], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: TransferData
    ) -> Any:
        """This method calls every update."""
        async with AsyncSession(bind=data['engine']) as session:
            data['db'] = Database(session)
            return await handler(event, data)
