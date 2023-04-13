FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

#ENV FLASK_RUN_HOST=0.0.0.0

#EXPOSE 5000

#CMD ["flask", "run"]
