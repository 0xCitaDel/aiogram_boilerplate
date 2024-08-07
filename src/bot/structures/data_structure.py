"""Data Structures.

This file contains TypedDict structure to store data which will
transfer throw Dispatcher->Middlewares->Handlers.
"""

from typing import TypedDict

from aiogram import Bot
from aiogram.types import User
from sqlalchemy.ext.asyncio import AsyncEngine

from bot.structures.role import Role
from db.database import Database

class TransferData(TypedDict):
    """Common transfer data."""

    db: Database
    engine: AsyncEngine
    event_from_user: User
    bot: Bot
    role: Role
