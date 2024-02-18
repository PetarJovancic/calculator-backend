import os
from dotenv import load_dotenv


load_dotenv()


class Settings():
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*")
    ALLOW_CREDENTIALS = bool(os.getenv('ALLOW_CREDENTIALS', True))
    ALLOW_METHODS = os.getenv('ALLOW_METHODS', "*")
    ALLOW_HEADERS = os.getenv('ALLOW_HEADERS', "*")
    HOST = os.getenv('HOST', "0.0.0.0")
    PORT = int(os.getenv('PORT', 8000))
    RELOAD = bool(os.getenv('RELOAD', True))


settings = Settings()
