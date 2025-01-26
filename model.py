from storage import Storage

class Model:

    def __init__(self):
        self.storage = Storage()

    def check_token(self, token: str):

        return self.storage.check_token(token)


    def add_user(self, telegram_id: int):
        return self.storage.add_user(telegram_id=telegram_id)


    def check_user(self, telegram_id: int):

        return self.storage.check_user(telegram_id=telegram_id)