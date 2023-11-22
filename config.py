"""
Конфигурационные параметры
"""
from dotenv import load_dotenv
from envparse import Env

load_dotenv()
env = Env()

TOKEN = env.str('TOKEN')
APP_PORT = env.int("APP_PORT", default=8080)
APP_HOST = env.str("APP_HOST", default="0.0.0.0")
WEBHOOK_TURN_ON = env.bool('WEBHOOK_TURN_ON', default=False)
WEBHOOK_TELEGRAM_URL = env.str('WEBHOOK_TELEGRAM_URL', default="")
WEBHOOK_TELEGRAM_PATH = env.str('WEBHOOK_TELEGRAM_PATH', default='/webhook')
WEBHOOK_SSL_CERT = env.str("WEBHOOK_SSL_CERT", default="")
