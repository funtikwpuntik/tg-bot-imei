from fastapi import FastAPI, Depends

from utils import get_imei_info, get_services as gs
from check_token import verify_token
app = FastAPI()


@app.post("/api/check-imei") # для получения данных по imei
async def check_imei(imei: str, token: str = Depends(verify_token)):

    return await get_imei_info(imei=imei)


@app.get("/api/get_services") # получение списка "сервисов"
async def get_services(token: str = Depends(verify_token)):
    return await gs()