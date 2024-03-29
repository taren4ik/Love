FROM python:3.11-slim

COPY ./  /app

RUN python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt

WORKDIR /app/love_prim/

CMD python manage.py runserver 0:5000

LABEL author='turgenevski@yandex.ru' version=1.0