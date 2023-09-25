from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
import app.keyboards as kb


router = Router()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [30075478]


@router.message(Admin(), F.text == '/admin')
async def admin_cmd(message: Message) -> None:
    await message.answer('You are an admin')


@router.message(F.text == '/start')
async def start_cmd(message: Message) -> None:
    await message.answer('Welcome!', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def catalog_cmd(message: Message) -> None:
    await message.answer('Our goods', reply_markup=kb.catalog)


@router.callback_query(F.data == 'adidas')
async def adidas_cb(callback: CallbackQuery) -> None:
    await callback.answer(f'You have chosen {callback.data}', show_alert=True)
