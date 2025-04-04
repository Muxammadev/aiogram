import os
from environs import Env

env = Env()
env.read_env()

__basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOT_TOKEN=env.str("BOT_TOKEN")
ADMIN=env.int("ADMIN")
DATABASE_URL = os.path.join(__basedir, "db.sqlite")