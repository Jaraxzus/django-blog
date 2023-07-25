# Django Блог

Проект "Django Блог" представляет собой простой веб-приложение на основе Django
с использованием Django REST Framework (DRF). Приложение позволяет пользователям
создавать посты, оставлять комментарии к постам, а также осуществлять
авторизацию через JWT токены. Все данные хранятся в базе данных PostgreSQL, а
для кэширования используется Redis. Проект также поддерживает запуск через
Docker Compose. Установка и запуск проекта

## Установка и запуск

Склонируйте репозиторий проекта:

```
git clone https://github.com/Jaraxzus/django-blog.git; cd django-blog
```

Создайте файл .env и заполните следующие поля:

```
SECRET_KEY=
POSTGRES_HOST=
POSTGRES_PASSWORD=
REDIS_HOST=
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=
```

Выполните команду для поднятия сервера:

```
docker-compose up -d
```

Создайте и примените миграции базы данных:

```
docker-compose exec django-blog python manage.py migrate
```

Создайте суперпользователя/админа:

```
docker-compose exec django-blog python manage.py createsuperuser
```

Перезапустите локальный сервер:

```
docker-compose restart django-blog
```

Теперь вы можете открыть веб-браузер и перейти по адресу
<http://localhost:8000/> для просмотра веб-приложения.

## Аутентификация и получение JWT токена

Для доступа к некоторым функциям приложения, таким как создание постов или
комментариев, требуется авторизация. Для этого вы должны выполнить запрос на
получение JWT токена.

Откройте приложение в браузере или используйте API клиент (например, Postman)
для выполнения HTTP запросов.

Зарегистрируйтесь или войдите в свою учетную запись. Для регистрации используйте
URL <http://localhost:8000/api/v1/auth/register/>, а для авторизации -
<http://localhost:8000/api/v1/auth/login/>.

После успешной авторизации вы получите JWT токен в ответе сервера. Для
дальнейшего доступа к защищенным функциям приложения, добавьте этот токен в
заголовок Authorization с префиксом Bearer, например:

```
Authorization: Bearer your_jwt_token_here
```

## API Endpoints

### Posts

Получить список всех постов.

```
GET /api/v1/blog/postlist/
```

Создать новый пост.

```
POST /api/v1/blog/postlist/
```

Получить информацию о конкретном посте по его ID.

```
GET /api/v1/blog/post/{id}/
```

Обновить информацию о конкретном посте.

```
PUT /api/v1/blog/post/{id}/
```

Удалить пост по его ID.

```
DELETE /api/v1/blog/post/{id}/
```

### Comments

Получить список всех комментариев, связанных с определенным постом.

```
GET /api/v1/blog/post/{post_id}/comments/
```

Создать новый комментарий к определенному посту.

```
POST /api/v1/blog/post/{post_id}/comments/
```

Получить информацию о конкретном комментарии по его ID, связанном с определенным
постом.

```
GET /api/v1/blog/post/{post_id}/comments/{id}/
```

Обновить информацию о конкретном комментарии, связанном с определенным постом.

```
PUT /api/v1/blog/post/{post_id}/comments/{id}/
```

Удалить комментарий по его ID, связанный с определенным постом. Authentication

```
DELETE /api/v1/blog/post/{post_id}/comments/{id}/
```

## Auth

Зарегистрировать нового пользователя.

```
POST /api/v1/auth/register/
```

Войти в систему существующим пользователем.

```
POST /api/v1/auth/login/
```

Выход из системы текущего пользователя.

```
POST /api/v1/auth/logout/
```

Получить информацию о текущем пользователе.

```
GET /api/v1/auth/user/
```

Запрос на сброс пароля.

```
POST /api/v1/auth/password/reset/
```

Подтверждение сброса пароля.

```
POST /api/v1/auth/password/reset/confirm/
```

Получить JWT токен после авторизации.

```
POST /api/v1/auth/token/
```

Обновить JWT токен.

```
POST /api/v1/auth/token/refresh/
```

## Admin Panel

Панель администратора Django.

```
/admin/
```

## Кэширование через Redis

Для кэширования данных проект использует Redis. Все данные постов и комментариев
кэшируются на 5 минут, что позволяет ускорить доступ к этим данным и снизить
нагрузку на базу данных. Запуск с помощью Docker Compose
