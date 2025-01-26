import json
import os
from datetime import datetime
from typing import Dict

import aiohttp
from dotenv import load_dotenv

load_dotenv()

# Запрос на получение информации по imei
async def get_imei_info(imei: str):
    url = 'https://api.imeicheck.net/v1/checks'
    data = json.dumps({
        'deviceId': imei,
        'serviceId': 12,
    })
    headers = {
        'Authorization': 'Bearer ' + os.environ['API_SERVICE'],
        'Content-Type': 'application/json',
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=data, headers=headers) as response:
            data = await response.json()

            return data['properties']

# Запрос на получение информации о "сервисах"
async def get_services():
    url = 'https://api.imeicheck.net/v1/services'
    headers = {
        'Authorization': 'Bearer ' + os.environ['API_SERVICE'],
        'Content-Type': 'application/json',
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            return await response.json()

# Запрос к апи для ТГ бота
async def api_get_imei_info(imei: str, token: str):
    url = 'http://127.0.0.1:8000/api/check-imei'
    params = {
        'imei': imei,
    }
    headers = {
        'Authorization': 'Bearer ' + token
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, params=params, headers=headers) as response:
            data = await response.json()

    return data

# Из полученных данных по IMEI в текст
def data_text(data: Dict):
    text = \
        f"Модель устройства: {data['deviceName']}\n" \
        f"imei: {data['imei']}\n" \
        f"meid: {data['meid']}\n" \
        f"imei2: {data['imei2']}\n" \
        f"Серийный номер: {data['serial']}\n" \
        f"Дата покупки: {datetime.fromtimestamp(data['estPurchaseDate'])}\n" \

    return text

# Сохранение картинки
async def get_image(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            name_image = url.split('/')[-1]
            with open(name_image, 'wb') as file:
                file.write(await response.read())

    return name_image

# Проверка на валидность IMEI
def valid_num(imei: str) -> bool:
    return True if imei.isdigit() and len(imei) == 15 and imei[0] == '3' else False
