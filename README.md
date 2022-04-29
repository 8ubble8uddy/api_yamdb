# Yamdb API

[![CI](https://github.com/8ubble8uddy/api_yamdb/workflows/yamdb-api/badge.svg
)](https://github.com/8ubble8uddy/api_yamdb/actions/workflows/yamdb_workflow.yml)

### **Описание**

_[yamdb-api](https://github.com/8ubble8uddy/yamdb-api) -  это REST API сервис. На этом сервисе пользователи могут оставлять к произведениям («Книги», «Фильмы», «Музыка») текстовые отзывы и ставить произведению оценку в диапазоне от одного до десяти. Из пользовательских оценок формируется рейтинг произведения._

### **Технологии**

```Python``` ```Django``` ```SQLite``` ```pytest``` ```Docker``` ```Gunicorn``` ```nginx```

### **Как запустить проект:**

Клонировать репозиторий и перейти внутри него в директорию ```infra/```:
```
git clone https://github.com/8ubble8uddy/yamdb-api.git
```
```sh
cd yamdb-api/infra/
```

Развернуть и запустить проект в контейнерах:
```
docker-compose up -d --build
```

Внутри контейнера ```web```:

- _Выполнить миграции_
  ```
  docker-compose exec web python manage.py migrate
  ```
- _Создать суперпользователя_
  ```
  docker-compose exec web python manage.py createsuperuser
  ```
- _Собрать статику_
  ```
  docker-compose exec web python manage.py collectstatic --no-input
  ```
- _Заполнить базу данных_
  ```
  docker-compose exec web python manage.py loaddata static/dump.json
  ```

**Проект будет доступен по адресу http://127.0.0.1/**

### Автор: Герман Сизов