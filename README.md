# Projet-Final-Structure

Launch docker config

> docker-compose up

Launch backend

> /app -> uvicorn main:app --reload

Launch frontend

> /frontend -> npm run dev

Access backend dev: http://localhost:8000

<!-- Access backend prod: http://localhost:5226 -->

Access FastApi docs: http://127.0.0.1:8000/docs

Front: http://localhost:3000

Access DB: http://localhost:8080

- System: PostgreSQL
- Server: db
- username: flamingo
- password: zeremi

Install requirement (for dev) without poetry:

> pip install fastapi uvicorn pydantic sqlalchemy sqlalchemy_utils python-dotenv psycopg2

Can also install with poetry and the pyproject.toml file.
- poetry shell

Ne pas oublier de rajouter: 
Fichier env/.env