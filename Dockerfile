FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt --no-cache-dir

CMD python manage.py runserver 0:8000

LABEL author='turgenevski@yandex.ru' version=1.0