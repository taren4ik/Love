***Статус проекта:***
![CI](https://github.com/taren4ik//actions/workflows/love_workflow.yml/badge.svg?branch=master)
![example workflow](https://github.com/taren4ik/love/actions/workflows/love_workflow.yml/badge.svg)


# Проект Love

### Описание. ###

Проект **Love**  является первой социальной сетью в приморском крае. 
В данном проекте создана кастомная модель User и форма регистрации. 
Добавлен функционал переписки между пользователями. Кроме того, 
реализована возможность множественной вставки изображений для 
создания мини-галереи в каждом профиле.


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

Для Unix-систем:
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
* Дмитрий  | Github:https://github.com/taren4ik/love
