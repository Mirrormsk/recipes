# Recipe book

API для хранения рецептов, позволяющее быстро найти рецепт который не содержит определенный продукт. 


## Настройка

Переименуйте файл `.env.example` в  `.env`, и внесите свои значения. 


## Запуск через Docker

```bash
docker compose up --build
```
### Создание суперпользователя:

Просмотр контейнеров

```bash
docker ps
```
Создание суперпользователя

```bash
docker exec -it <hash контейнера api> python3 manage.py csu
```


## Локальный запуск

Создайте виртуальное окружение

```bash
python3 -m venv venv
```

Установите зависимости

через pip:

```bash
pip install -r requirements.txt
```

через poetry:
```bash
poetry install
```

Примените миграции:
```bash
python3 manage.py migrate
```

Создайте суперпользователя:
```bash
python3 manage.py csu
```
