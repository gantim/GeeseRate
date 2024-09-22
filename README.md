# GeeseRate

GeeseRate — это веб-приложение для оценки учебных заведений, разработанное на Django. 
Оно позволяет пользователям оставлять отзывы и оценки для различных учебных заведений.

![GitHub release](https://img.shields.io/github/v/release/gantim/GeeseRate)
![License](https://img.shields.io/github/license/gantim/GeeseRate)

## Содержание
- [Описание](#описание)
- [Установка](#установка)
- [Использование](#использование)
- [Скриншоты](#скриншоты)
- [Лицензия](#лицензия)

## Установка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/gantim/GeeseRate.git
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
3. Настройте базу данных:
    ```bash
    python manage.py migrate

## Использование

Запустите сервер:
    ```bash
    python manage.py runserver

API Swagger - http://127.0.0.1:8000/swagger/
API Redoc - http://127.0.0.1:8000/redoc/
