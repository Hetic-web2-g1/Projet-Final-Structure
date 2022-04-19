# Projet-Final-Structure

$ docker build -t my-python-app .
$ docker run -it --rm --name my-running-app my-python-app

docker compose up
python main.py

<!-- docker-compose --env-file .env config
docker-compose --env-file .env up -->

poetry shell package manager
sql alchemy

DB: http://localhost:8080
/frontend -> npm run dev
Front: http://localhost:3000
Backend: http://localhost:5226
from pydantic import BaseSettings

class Config(BaseSettings):
origin_email: str
origin_pass: str
database_url: str

    class Config:
        env_file = '.env'

settings = Config()
