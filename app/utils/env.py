from dotenv import load_dotenv
import os

load_dotenv("../env/.env")

db_type = os.environ['DB_TYPE']
db_url = os.environ['DB_URL']
db_user = os.environ['DB_USER']
db_pswd = os.environ['DB_PSWD']
db_name = os.environ['DB_NAME']