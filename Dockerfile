FROM python:3.6-slim

WORKDIR .

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

COPY app app
COPY config config
COPY instance instance

EXPOSE 5000

CMD FLASK_APP=app/app.py flask run


