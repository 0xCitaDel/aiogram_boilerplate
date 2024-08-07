from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot import states as st


async def some_handler(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
    ):
    await manager.switch_to(st.MainSG.start)


async def go_main(
        callback: CallbackQuery,
        widjet: Button,
        dialog_manager: DialogManager
    ):
    await dialog_manager.switch_to(st.MainSG.start)


async def go_back(
        callback: CallbackQuery,
        widjet: Button,
        dialog_manager: DialogManager
    ):
    await dialog_manager.back()

