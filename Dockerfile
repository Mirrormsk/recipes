FROM python:3.12
LABEL authors="maxim"

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry gunicorn

COPY ./poetry.lock .
COPY ./pyproject.toml .


RUN poetry  config virtualenvs.create false --local && poetry install
COPY . .