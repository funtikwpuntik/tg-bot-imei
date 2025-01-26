from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InputMediaPhoto

from model import Model
import os
from dotenv import load_dotenv

from utils import api_get_imei_info, data_text, get_image, valid_num

load_dotenv()
router = Router()

# Команда start, она же выдает токен при активации бота
@router.message(Command('start'))
async def start(message: Message):
    model = Model()
    token = model.add_user(message.chat.id)
    await message.answer(f'Hi!\nВаш токен:\n{token}')


# Принимает любые сообщения для обработки IMEI
@router.message()
async def check_imei(message: Message):
    model = Model()
    telegram_id = message.chat.id
    ans_message = await message.answer('Загрузка...')
    user = model.check_user(telegram_id=telegram_id)
    if user[-1]:
        if valid_num(message.text):
            data = await api_get_imei_info(message.text, user[0])
            text = data_text(data)
            await ans_message.edit_text(text=text)
            filename = await get_image(data['image'])
            image = FSInputFile(path=filename, filename=filename)

            await ans_message.edit_media(media=InputMediaPhoto(media=image, caption=text))
            os.remove(filename)
        else:
            await ans_message.edit_text(text='Неверный IMEI')
    else:
        await ans_message.edit_text(text='Нет доступа')