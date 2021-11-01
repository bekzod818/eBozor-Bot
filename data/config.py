from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
# To'lov TOKENI
PROVIDER_TOKEN_CLICK = env.str("PROVIDER_TOKEN_CLICK")
PROVIDER_TOKEN_PAYME = env.str("PROVIDER_TOKEN_PAYME")
PROVIDER_TOKEN_TR = env.str("PROVIDER_TOKEN_TR")
# Postgres SQL
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
