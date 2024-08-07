from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot import states as st

from . import handlers
from . import getters


main_window = Window(
        Const('Welcome 📁'),
        Button(
            Const('Button'),
            id='some_btn',
            on_click=handlers.some_handler
        ),
        getter=getters.main_getter,
        state=st.MainSG.start,
    )


main_dialog = Dialog(
    main_window,
)
