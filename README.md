# Приложение для Благотворительного фонда

Фонд собирает пожертвования на различные целевые проекты. Интерфейс: API, Google spreadsheets

##### Проекты
В Фонде может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
##### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.
##### Пользователи
Целевые проекты создаются администраторами сайта. Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых. Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.


###  Установка и настройки
  * Шаг первый: клонируем репозиторий
```python
git@github.com:Nurbek878/QRkot_spreadsheets.git
```
 * Переходим в папку с проектом 
```sh 
cd QRkot_spreadsheets
``` 
* Создаем и активируем виртуальное окружение 
```sh 
python -m venv venv 
source venv/bin/activate 
``` 
* Обновляем менеджер пакетов pip
```sh 
pip install --upgrade pip 
``` 
* Устанавливаем необходимые зависимости 
```sh 
pip install -r requirements.txt
``` 
* В корне проекта создаем .env файл
```sh 
APP_TITLE=Name
APP_DESCRIPTION=Description
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=Your_secret
FIRST_SUPERUSER_EMAIL=first@mail.ru
FIRST_SUPERUSER_PASSWORD=Your_first_user_password
EMAIL=<USER_EMAIL>
TYPE=service_account
PROJECT_ID=<PROJECT_ID>
PRIVATE_KEY_ID=<PRIVATE_KEY_ID>
PRIVATE_KEY=<PRIVATE_KEY>
CLIENT_EMAIL=<CLIENT_EMAIL>
CLIENT_ID=<CLIENT_ID>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<CLIENT_ID>
``` 
* Применяем миграции для создания таблиц в БД
```sh 
alembic upgrade head
``` 
* Запускаем приложение командой
```sh 
uvicorn app.main:app --reload
``` 
Приложение доступно по следующему адресу http://127.0.0.1:8000


В приложении доступны endpoints:
    
* #####    Charity projects

```sh
GET, POST      /charity_project/ - получение данных по всем проектам, создание нового проекта (для суперюзеров)
PATCH, DELETE  /charity_project/{project_id} - изменение, удаление существующего проекта (для суперюзеров)
``` 
* #####   Donations
```sh
GET     /donation/ - получение списка всех пожертвований (для суперюзеров)
POST    /donation/ - создание пожертвования
GET     /donation/my - получение списка всех пожертвований пользователя
``` 
* #####    Auth
```sh
POST    /auth/register - регистрация пользователя
POST    /auth/jwt/login - получение пользователем jwt-токена
POST    /auth/jwt/logout - сброс jwt-токена
``` 
* #####    Users
```sh
GET, PATCH           /users/me - изменение и получение данных пользователя
GET, PATCH, DELETE   /users/{id} - получение, изменение, удаление (не используется, деактивация) пользователей
``` 
* #####    Google
```sh
POST           /google/ - создания гугл-таблицы  на диске вашего сервисного аккаунта с отчётом по закрытым проектам, отсортированным по скорости сбора средств
``` 

### Стек
-   [Python](https://www.python.org/)
-   [FastAPI](https://fastapi.tiangolo.com/)
-   [SQLAlchemy](https://www.sqlalchemy.org/)
-   [Alembic](https://alembic.sqlalchemy.org)

### Автор

- [@nurbek878](https://github.com/Nurbek878)