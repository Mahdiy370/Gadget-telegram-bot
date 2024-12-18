from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text= 'Shop'),KeyboardButton(text= 'Aloqa')],
    ],
    resize_keyboard=True
)
tex=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Maishiy texnika'),KeyboardButton(text='Kiyim'),KeyboardButton(text='Gatgetlar')]
    ],
    resize_keyboard=True
)   


gagetlar=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon'),KeyboardButton(text='Kompyuter'),KeyboardButton(text='Planshet')],
        [KeyboardButton(text='Orqaga')]

    ],
    resize_keyboard=True
)


kiyim1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Gucci'),KeyboardButton(text='Louis Vuitton'),KeyboardButton(text='Lacoste'),KeyboardButton(text='Nike')],
        [KeyboardButton(text='Orqaga')]

    ],
    resize_keyboard=True
)


texnika2=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Mikravolnovka'),KeyboardButton(text='Kanditsioner'),KeyboardButton(text='Televizor'),KeyboardButton(text='Gaz Plita')],
        [KeyboardButton(text='Orqaga')]

    ],
    resize_keyboard=True
)