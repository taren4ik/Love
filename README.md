# Проект Love

### Описание. ###

Проект **Love**  является первой социальной сетью в приморском крае


***


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
bash
git clone https://github.com/taren4ik/Love
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
bash
python -m venv venv
```

Для *nix-систем:
```
bash
source venv/bin/activate
```

Для windows-систем:
```
bash
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
bash
cd api_yamdb
python3 manage.py migrate
```

Создать суперпользователя (для раздачи прав админам):

```
bash
python manage.py createsuperuser
```

Запустить проект:

```
bash
python manage.py runserver
```

Сам проект и админ-панель искать по адресам:
```
bash
http://127.0.0.1:8000
http://127.0.0.1:8000/admin
```

***Автор проекта:***
* Дмитрий Пермяков | Github:https://github.com/taren4ik | Разработчик, написание части с отзывами (Review) и комментариями (Comments): описание модели, представления, настройка эндпойнтов, определение прав доступа для запросов. Рейтинги произведений.


[![CI](https://github.com/yandex-praktikum//actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml)
