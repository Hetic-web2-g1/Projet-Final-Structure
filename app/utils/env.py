# from dotenv import load_dotenv
# import os
# from utils.log import *

# load_dotenv()

# db_type = os.environ['DB_TYPE']
# logging.info(db_type)
# db_url = os.environ['DB_URL']
# db_user = os.environ['DB_USER']
# db_pswd = os.environ['DB_PSWD']
# db_name = os.environ['DB_NAME']

# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     DB_TYPE: str
#     DB_URL: str
#     DB_USER: str
#     DB_PSWD: str
#     DB_NAME: str

#     class Config:
#         env_file = os.path.expanduser('env/.env')


# settings = Settings()
