# Backend

FROM python:3.10.4

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install -U pip \
    && apt-get update \
    && apt install -y curl netcat \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /code

COPY pyproject.toml /code 

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
  
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "5226"]