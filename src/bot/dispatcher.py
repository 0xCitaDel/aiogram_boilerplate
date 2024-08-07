from typing import Optional

from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy

from aiogram_dialog import setup_dialogs
from bot.middlewares.database import DatabaseMiddleware
from bot.middlewares.check_access import CheckAccessMiddleware
from bot.middlewares.permissions import PermissionMiddleware

from bot.handlers import routers
from bot.structures.role import Role


def get_dispatcher(
    storage: BaseStorage = MemoryStorage(),
    fsm_strategy: Optional[FSMStrategy] = FSMStrategy.CHAT,
    event_isolation: Optional[BaseEventIsolation] = None,
):
    """This function set up dispatcher with routers, filters and middlewares"""
    dp = Dispatcher(
        storage=storage
    )

    dp.update.outer_middleware(DatabaseMiddleware())
    dp.update.outer_middleware(CheckAccessMiddleware())
    dp.update.outer_middleware(PermissionMiddleware(Role.SUBSCRIBER))

    setup_dialogs(dp)

    for router in routers:
        dp.include_router(router)

    return dp
