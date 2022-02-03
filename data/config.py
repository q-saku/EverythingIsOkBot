from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
HOST = env.str("HOST")
PORT = env.str("PORT")

# DB preferences
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
POSTGRES_URI = f"postgres://{PGUSER}:{PGPASSWORD}@{HOST}:{PORT}/{DATABASE}"
