import configparser
import random
import string

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        email = config.get("common info", "email")
        return email

    @staticmethod
    def getUserPassword():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    username = generate_random_string(3)
    domain = random.choice(["gmail.com"])
    random_email = f"{username}@{domain}"
    print(random_email)

    @staticmethod
    def generate_random_password(length=6):
        characters = string.ascii_letters + string.ascii_uppercase + string.hexdigits
        password2 = ''.join(random.choice(characters) for _ in range(length))
        return password2

    # Usage example:
    random_password = generate_random_password()
    # print(random_password)

