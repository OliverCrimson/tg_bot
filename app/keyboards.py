from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

keyboard_main = [
    [KeyboardButton(text='Catalog'),
     KeyboardButton(text='Card')],
    [KeyboardButton(text='Profile'),
     KeyboardButton(text='Contacts')],
]

main = ReplyKeyboardMarkup(keyboard=keyboard_main,
                           resize_keyboard=True,
                           input_field_placeholder='Choose any option below')

contacts_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/sample')],
    [InlineKeyboardButton(text='Facebook', url='https://t.me/sample')],
    [InlineKeyboardButton(text='Website', url='https://t.me/sample')],
])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Adidas', callback_data='adidas')],
    [InlineKeyboardButton(text='Nike', callback_data='nike')],
    [InlineKeyboardButton(text='New Balance', callback_data='new_balance')],
])