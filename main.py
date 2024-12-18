import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN as token
from button import *


bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menu)

# 'Shop' tugmasi uchun handler
@dp.message(F.text == 'Shop')
async def shop1(message: Message):
    await message.answer_photo(photo='https://mma.prnewswire.com/media/2067732/4015311/Uzum_Group_Logo.jpg?p=facebook', caption='Magazinga Xushkelibsiz', reply_markup=tex)

# 'Maishiy texnika' tugmasi uchun handler
@dp.message(F.text == 'Maishiy texnika')
async def shop2(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/get-altay/5456749/2a0000017ee8b6d5465bbb2b18a60a3c5127/XXL_height', caption='Texnika', reply_markup=texnika2)

# 'Kiyim' tugmasi uchun handler
@dp.message(F.text == 'Kiyim')
async def shop3(message: Message):
    await message.answer_photo(photo='https://ae01.alicdn.com/kf/H5b8e84e54a6d40f9916b8ab95d4af3dbQ/7XL-6XL.jpg', caption='Mana kiyim arzon narxda 150 ming som', reply_markup=kiyim1)

# 'Gadgetlar' tugmasi uchun handler
@dp.message(F.text == 'Gatgetlar')
async def shop4(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=be0bcc471f176e34c5c9f4351884f9d2c00ddddf-4034411-images-thumbs&n=13', caption='Mana Gadgetlar juda zor va arzon', reply_markup=gagetlar)


@dp.message(F.text == 'Planshet')
async def shop4(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=608201e4b489f8e48de1e841dcb634b36aa74e54-5584275-images-thumbs&n=13', caption='Mana planshet juda sifatli narxi 700$', reply_markup=gagetlar)


@dp.message(F.text == 'Kompyuter')
async def shop4(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=b130b35f88695e17d43b3e01c84ac6c510b3c3f0-5876743-images-thumbs&n=13', caption='Mana kompyuterimiz juda sifatli narxi 750$', reply_markup=gagetlar)



@dp.message(F.text == 'Telefon')
async def shop4(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=fbfa83c4e0d1b731a5007cd2c5c4f983ca0f96f3-13461479-images-thumbs&n=13', caption='Mana telefon boshlangich narxi 400$', reply_markup=gagetlar)

@dp.message(F.text == 'Gucci')
async def shop4(message: Message):
    await message.answer_photo(photo='https://i.pinimg.com/736x/4d/ac/a1/4daca1d7051f0ebbfc1ca6d0752793b1.jpg', caption='Mana Gucci brend kiyimi juda zor narxi 600$', reply_markup=kiyim1)


@dp.message(F.text == 'Louis Vuitton')
async def shop4(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=d2128ebc607cec6fc165c9598da3c72f_l-7051630-images-thumbs&n=13', caption='Mana Louis Vuitton brend kiyimi juda zor narxi 620$', reply_markup=kiyim1)

@dp.message(F.text == 'Lacoste')
async def shop4(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=45ba0e8a8e86065be0907ed7d0edf99c_l-3986671-images-thumbs&n=13', caption='Mana Lacoste brend kiyimi juda zor narxi 100$', reply_markup=kiyim1)


@dp.message(F.text == 'Nike')
async def shop4(message: Message):
    await message.answer_photo(photo='https://cdn1.ozone.ru/s3/multimedia-u/6371069958.jpg', caption='Mana Nike brend kiyimi juda zor narxi 100$', reply_markup=kiyim1)


@dp.message(F.text == 'Mikravolnovka')
async def shop4(message: Message):
    await message.answer_photo(photo='https://assets.asaxiy.uz/product/items/desktop/1d496b5dadd98a748ad1f5488646c1a92020031313534016064SuqBS08Ulr.jpg.webp', caption='Mana Mikravolnovka juda zor narxi 400 ming som', reply_markup=texnika2)


@dp.message(F.text == 'Konditsioner')
async def shop4(message: Message):
    await message.answer_photo(photo='', caption='Mana Konditsioner juda zor narxi 400 ming som', reply_markup=texnika2)


@dp.message(F.text == 'Konditsioner')
async def shop4(message: Message):
    await message.answer_photo(photo='', caption='Mana Konditsioner juda zor narxi 400 ming som', reply_markup=texnika2)



@dp.message(F.text == 'Orqaga')
async def shop4(message: Message):
    await message.answer(text='Asosiy Menu',reply_markup=tex)

# Botni ishga tushirish uchun asosiy funksiya
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())