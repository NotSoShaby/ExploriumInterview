
FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN pip install -r requirements.txt

COPY application.py /app
COPY __init__.py /app

ADD calculators /app/app/calculators
ADD db_helper /app/app/db_helper
ADD infra /app/app/infra

ENTRYPOINT python application.py
