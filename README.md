# GeeseRate

GeeseRate — это веб-приложение для оценки учебных заведений, разработанное на Django. 
Оно позволяет пользователям оставлять отзывы и оценки для различных учебных заведений.

![Python](https://img.shields.io/badge/python-3.12.6-blue)
![Django](https://img.shields.io/badge/Django-5.1.1-green)
![Django REST Framework](https://img.shields.io/badge/DRF-3.15.2-green)

## Содержание
- [Установка](#установка)
- [Использование](#использование)

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

- Запустите сервер:
    ```bash
    python manage.py runserver   

- API
  - Swagger:
    ```bash
    http://127.0.0.1:8000/swagger/
  - Redoc
    ```bash
    http://127.0.0.1:8000/redoc/

Test
