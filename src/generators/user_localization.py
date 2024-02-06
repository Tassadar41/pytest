from faker import Faker

fake = Faker()


class UserLocalization :

    def __init__(self, language):
        self.fake = Faker(language)
        self.result = {
            'nickname': self.fake.first_name()
        }

    def build(self):
        return self.result
