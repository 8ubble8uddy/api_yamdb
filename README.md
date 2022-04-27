# Yamdb API

[![CI](https://github.com/8ubble8uddy/api_yamdb/workflows/Yamdb/badge.svg
)](https://github.com/8ubble8uddy/api_yamdb/actions/workflows/yamdb_workflow.yml)

### **Описание**

_Проект [YaMDb](https://github.com/8ubble8uddy/api_yamdb) собирает отзывы пользователей на различные произведения_

### **Технологии**

```Python``` ```Docker``` ```Django``` ```SQLite``` ```Gunicorn``` ```nginx```

### **Как запустить проект:**

Клонировать репозиторий и перейти внутри него в директорию ```infra/```:
```
git clone https://github.com/8ubble8uddy/api_yamdb.git
```
```sh
cd api_yamdb/infra/
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