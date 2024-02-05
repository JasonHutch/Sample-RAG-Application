FROM python:3.10.13-slim-bullseye
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt