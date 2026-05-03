# FastAPI Ads Service

Сервис объявлений купли/продажи, реализованный на FastAPI с использованием PostgreSQL и Docker.

---

## 📌 Описание

Приложение предоставляет REST API для работы с объявлениями.
Поддерживаются базовые CRUD-операции и поиск по параметрам.

---

## ⚙️ Стек технологий

* Python 3.11
* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker / Docker Compose

---

## 🚀 Запуск проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-username/fastapi-ads.git
cd fastapi-ads
```

### 2. Запустить контейнеры

```bash
docker compose up --build
```

---

## 🌐 Доступ к API

После запуска приложение доступно по адресу:

```
http://localhost:8000
```

Swagger-документация:

```
http://localhost:8000/docs
```

---

## 📦 Структура проекта

```
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📌 API Эндпоинты

### ➕ Создание объявления

```
POST /advertisement
```

Пример запроса:

```json
{
  "title": "iPhone 15",
  "description": "Новый",
  "price": 1000,
  "author": "Ivan"
}
```

---

### 🔍 Получение объявления

```
GET /advertisement/{id}
```

---

### ✏️ Обновление объявления

```
PATCH /advertisement/{id}
```

Пример:

```json
{
  "price": 900
}
```

---

### ❌ Удаление объявления

```
DELETE /advertisement/{id}
```

---

### 🔎 Поиск объявлений

```
GET /advertisement?title=...&author=...
```

Примеры:

```
/advertisement?title=iPhone
/advertisement?author=Ivan
```

---

## 🗄 Модель данных

Объявление содержит поля:

* `id` — уникальный идентификатор
* `title` — заголовок
* `description` — описание
* `price` — цена
* `author` — автор
* `created_at` — дата создания

---

## ⚠️ Примечания

* Аутентификация и авторизация не реализованы (не требуются по заданию)
* База данных автоматически создаётся при запуске
* При первом запуске Docker может скачивать образы (это нормально)

---

## ✅ Готово

Проект полностью готов к запуску и тестированию через Swagger UI.
