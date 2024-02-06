from src.enums.statuses import Statuses
from src.generators.user_localization import UserLocalization


class User:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balanse(self, balance=0):
        self.result['balance'] = balance
        return self

    def reset(self):
        self.set_status()
        self.set_balanse()
        self.result['localization'] = {
                "en": UserLocalization('en_US').build(),
                "ru": UserLocalization('ru_RU').build()
            }
        return self

    def build(self):
        return self.result


z = User().build()
print(z)
