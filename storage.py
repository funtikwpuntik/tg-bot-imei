from sqlalchemy import create_engine, select, insert

from db_models import Users
from gen_token import generate_token


# Класс для работы с данными о лотах
class Storage:

    def __init__(self):
        # Создание соединения с базой данных SQLite
        self.engine = create_engine("sqlite+pysqlite:///database.db", echo=True)
        self.session = self.engine.connect()


    def check_token(self, token: str):

        result = self.session.execute(
            select(Users).where(Users.api_token == token)
        ).first()

        self.session.close()
        if result:
            return result[-2]
        return {'error': "Invalid API token"}

    def add_user(self, telegram_id: int):

        user = self.session.execute(
            select(Users.api_token).where(Users.telegram_id == telegram_id)
        ).first()
        if user:
            return user[0]
        token = generate_token()
        self.session.execute(
        insert(Users), {
            'telegram_id': telegram_id,
            'api_token': token,
            'allow': True,
        }
    )
        self.session.commit()
        self.session.close()
        return token

    def check_user(self, telegram_id: int):

        return self.session.execute(
            select(Users.api_token, Users.allow).where(Users.telegram_id == telegram_id)
        ).first()
