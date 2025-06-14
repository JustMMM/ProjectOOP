# Clean Architecture Blog Project

## Описание

Проект блога, реализованный в качестве задания по предмету "Объектно-ориентированное программирование в мобильной разработке и WEB-разработке" с использованием архитектуры Clean Architecture. Поддерживает создание пользователей, постов и комментариев. Используется FastAPI и SQLite.

## Стек технологий

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Postman

## Установка

1. Клонируйте репозиторий:


git clone https://github.com/username/blog.git
cd blog


2. Создайте виртуальное окружение и активируйте его:


python -m venv venv
source venv/bin/activate # для Linux/macOS
venv\Scripts\activate # для Windows


3. Установите зависимости:

pip install -r requirements.txt


## Запуск

Запустите приложение с помощью Uvicorn:

uvicorn main:app --reload


API будет доступен по адресу:

http://127.0.0.1:8000


Документация Swagger:

http://127.0.0.1:8000/docs


## Работа с Postman

В папке `postman/` находится коллекция запросов:  
`blog_api_collection.json`

Импортируйте её в Postman и используйте следующие запросы:

- `POST /users` — создание пользователя
- `POST /posts` — создание поста
- `POST /comments` — добавление комментария
- `GET /posts/{post_id}` — получить пост с комментариями

## Автор

Матвеев Максим Максимович
БПИ-22-4
2025
