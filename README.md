## Foodgram - это площадка для публикации рецетов. Реализована возможность подписываться на авторов и добавлять рецепты к себе в избранное. Также можно скачать список покупок ингредиентов рецепта.

<img src="https://github.com/eltimccc/foodgram-project-react/actions/workflows/main.yml/badge.svg"><br>  
### Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Подготовка и запуск проекта
* Склонировать репозиторий на локальную машину:
```
git clone https://github.com/eltimccc/foodgram-project-react
```

## Для работы с удаленным сервером в YandexCloud:

* Подключитесь к своей виртуальной машине
```
ssh <your_login>c@<your.ip>
```

* Установите docker на виртуальный сервер:
```
sudo apt install docker.io 
```
* Установите docker-compose на сервер:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
* Необходимо иметь высокую степень решения , чтобы сделать команду docker-compose исполняемой:
```
sudo chmod +x /usr/local/bin/docker-compose
```
* Локально отредактируйте файл infra/nginx.conf и в строке server_name впишите свой IP-адрес виртуальной машины

* Скопируйте файлы docker-compose.yml и nginx.conf из директории infra на сервер:
```
scp docker-compose.yml <username>@<host>:/home/<your_login>/docker-compose.yml
scp nginx.conf <your_login>c@<your.ip>:/home/<your_login>/nginx.conf
```

* Необходимо заполнить .env в директории foodgram-project-react/backend/foodgram/ файл, пример:

```
DB_ENGINE="django.db.backends.postgresql"
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD="postgres"
DB_HOST='db'
DB_PORT='5432'
SECRET_KEY="<django-secret-key>"
```
* Для работы с Workflow добавьте в Secrets GitHub *(project -> Settings -> Secrets and variables -> Actions)* переменные окружения для работы:
```
DB_ENGINE=<django.db.backends.postgresql>
DB_HOST=<db>
DB_NAME=<имя бд postgres>
DB_PORT=<5432>
POSTGRESS_USER=<имя пользователя postgres>
POSTGRES_PASSWORD=<пароль от бд postgress>

DOCKER_PASSWORD=<пароль от аккаунта Docker>
DOCKER_USERNAME=<имя пользователя Docker>

HOST=<ip адрес облачного сервера>
USER=<имя пользователя облачного сервера>
PASSPHRASE=<пароль от облачного сервера>
SECTRET_KEY=<django-secret-key>
SSH_KEY=<Ваш SSH ключ>

TELEGRAM_TO=<телеграм айди того, кому придет уведомление>
TELEGRAM_TOKEN=<тоекен телеграм бота>
```
В Workflow четыре шага:

- Проверка кода на соответствие PEP8
- Сборка и публикация образа бекенда на - DockerHub.
- Автоматический деплой на удаленный сервер.
- Отправка уведомления в телеграм-чат.

* Сборка docker-compose в облаке:
```
sudo docker-compose up -d --build
```
* После запуска проекта, собираем статику:
```
sudo docker-compose exec backend python manage.py collectstatic --noinput
```
* Применяем миграции
```
sudo docker-compose exec backend python manage.py migrate --noinput
```

### Наслаждаемся запущенным проектом в облаке!
### Автор
[Денис М. (Python-разработчик)](https://github.com/Eltimccc "Денис М (Python-разработчик)")
