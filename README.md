# GeeseRate

GeeseRate — это веб-приложение для оценки учебных заведений, разработанное на Django. Оно позволяет пользователям оставлять отзывы и оценки для различных учебных заведений, курсов и преподавателей.

![Python](https://img.shields.io/badge/Python-3.12.6-blue)
![Django](https://img.shields.io/badge/Django-5.1.1-green)
![Django REST Framework](https://img.shields.io/badge/DRF-3.15.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)

---

## Содержание

- [Описание проекта](#описание-проекта)
- [Технологии](#технологии)
- [Установка](#установка)
  - [Подготовка окружения](#подготовка-окружения)
  - [Настройка базы данных](#настройка-базы-данных)
  - [Миграции](#миграции)
  - [Запуск](#запуск)
- [Документация API](#документация-api)
- [Полезная информация](#полезная-информация)

---

## Описание проекта

GeeseRate предоставляет платформу для:
- Оценки и обзора учебных заведений.
- Создания курсов и расписаний.
- Управления отзывами, включая возможность добавления рейтингов и комментариев.

Проект использует Django для серверной части и предоставляет API, которое может быть интегрировано с фронтендом.

---

## Технологии

- **Python** 3.12.6 — основной язык разработки.
- **Django** 5.1.1 — фреймворк для построения веб-приложений.
- **Django REST Framework** 3.15.2 — для реализации API.
- **PostgreSQL** 15 — реляционная база данных.
- **Swagger/Redoc** — для автоматической документации API.
- **qrcode** — для генерации QR-кодов.

---

## Установка

### Подготовка окружения

1. **Склонируйте репозиторий:**
   ```bash
   git clone https://github.com/gantim/GeeseRate.git
   cd GeeseRate

2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Linux/MacOS
   .venv\Scripts\activate     # Для Windows

3. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt

### Настройка базы данных

1. **Убедитесь, что PostgreSQL установлен и запущен.**

2. **Создайте базу данных:**
   ```sql
   CREATE DATABASE geeserate;
   CREATE USER geese_user WITH PASSWORD 'your_password';
   ALTER ROLE geese_user SET client_encoding TO 'utf8';
   ALTER ROLE geese_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE geese_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE geeserate TO geese_user;

3. **Обновите настройки базы данных в settings.py:**
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'geeserate',
        'USER': 'geese_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
   }
