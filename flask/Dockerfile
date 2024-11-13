<<<<<<< Updated upstream
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /flask

COPY requirements.txt /flask/requirements.txt
RUN pip install -r requirements.txt

COPY app /flask/app
COPY config.py /flask/config.py
COPY wsgi.py /flask/wsgi.py

<<<<<<< HEAD
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
=======
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /flask

COPY requirements.txt /flask/requirements.txt
RUN pip install -r requirements.txt

COPY app /flask/app
COPY config.py /flask/config.py
COPY wsgi.py /flask/wsgi.py

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile=access.log", "--error-logfile=error.log", "wsgi:app"]
>>>>>>> Stashed changes
=======
CMD ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile=access.log", "--error-logfile=error.log", "wsgi:app"]
>>>>>>> d5a6d6f08f3a58e5cfa408aece902ee5d159314f
