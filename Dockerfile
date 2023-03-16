FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

CMD python manage.py runserver 0:5000

LABEL author='turgenevski@yandex.ru' version=1.0