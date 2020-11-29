FROM python:3.8-slim

RUN mkdir /application

COPY ./requirements.txt /application

WORKDIR /application

RUN apt-get update

RUN apt-get install python3-dev default-libmysqlclient-dev gcc -y

RUN pip install -r requirements.txt

ENV FLASK_CONFIG=development

ENV FLASK_APP=run.py

COPY . .

CMD ["python", "run.py"]

