FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /ghost_fnk 

COPY . .
RUN pip install setuptools --upgrade 
RUN apt-get update && apt-get install -y libpq-dev build-essential gcc
RUN pip install --no-cache-dir --requirement requirements.txt