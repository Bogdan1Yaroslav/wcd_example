import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
VICTIM_USER_PASS = os.getenv("VICTIM_USER_PASS")
TOKEN_EXPIRE_PERIOD = int(os.getenv("TOKEN_EXPIRE_PERIOD", "1"))
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

USERS = {
    'victim_user': VICTIM_USER_PASS
}
