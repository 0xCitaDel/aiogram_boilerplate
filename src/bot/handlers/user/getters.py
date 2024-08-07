import os

from aiogram_dialog import DialogManager

from db.database import Database


async def main_getter(
        dialog_manager: DialogManager,
        db: Database,
        **kwargs
    ):
    return {'data': 'some_data'}
