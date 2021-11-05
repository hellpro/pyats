
FROM python:3.8.0

MAINTAINER Kirill Fedotov <kemt.info@gmail.com>

ENV TZ=Europe/Moscow
WORKDIR /app
COPY pyats .
RUN pip install --upgrade pip setuptools
RUN pip install pyats[full]
