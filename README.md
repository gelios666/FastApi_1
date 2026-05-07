FastAPI Advertisement Service

Сервис объявлений купли/продажи, реализованный на FastAPI с использованием PostgreSQL и Docker.

📌 Возможности API

Поддерживаются следующие операции:
Создание объявления
Получение объявления по ID
Обновление объявления
Удаление объявления
Поиск объявлений
Фильтрация по цене
Пагинация результатов

🛠 Используемые технологии
Python 3.11
FastAPI
SQLAlchemy
PostgreSQL
Docker
Docker Compose
Pydantic

📂 Структура проекта
.
├── app
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🚀 Запуск проекта
1. Клонирование репозитория
git clone <repository_url>
cd FastApi_1
2. Запуск через Docker
docker compose up --build

🌐 Swagger документация
После запуска API будет доступно:

http://localhost:8000/docs
🗄 PostgreSQL

Контейнер PostgreSQL запускается автоматически через Docker Compose.

Параметры подключения:

DB: advertisements_db
USER: postgres
PASSWORD: postgres
HOST: db
PORT: 5432

📌 Модель объявления

Объявление содержит поля:

Поле	Тип
id	integer
title	string
description	string
price	float
author	string
created_at	datetime
📡 API endpoints
➕ Создание объявления
POST /advertisement
Пример запроса
{
  "title": "iPhone 15",
  "description": "New phone",
  "price": 1000,
  "author": "Ivan"
}
Успешный ответ
201 Created
📄 Получение объявления
GET /advertisement/{id}
Пример
GET /advertisement/1
✏️ Обновление объявления
PATCH /advertisement/{id}
Пример запроса
{
  "price": 1200
}
❌ Удаление объявления
DELETE /advertisement/{id}
Успешный ответ
204 No Content
🔎 Поиск объявлений
GET /advertisement

Поддерживаются параметры:

Параметр	Описание
title	поиск по заголовку
author	поиск по автору
min_price	минимальная цена
max_price	максимальная цена
limit	количество записей
offset	смещение
📌 Примеры поиска
Поиск по title
GET /advertisement?title=iphone
Фильтр по цене
GET /advertisement?min_price=100&max_price=1000
Пагинация
GET /advertisement?limit=5&offset=10
Комбинированный поиск
GET /advertisement?title=iphone&author=ivan&min_price=500
✅ Валидация

API проверяет:

обязательные поля
типы данных
цену (price > 0)
пустые строки title/author

При невалидных данных возвращается:

422 Unprocessable Entity
🐳 Docker

В проекте используются:

Dockerfile — сборка FastAPI приложения
docker-compose.yml — запуск API и PostgreSQL

Для PostgreSQL добавлен healthcheck, чтобы приложение запускалось только после готовности базы данных.

📌 Проверка работы

После запуска:

Открыть Swagger:

http://localhost:8000/docs
Создать объявление
Проверить:
получение
обновление
удаление
поиск
пагинацию