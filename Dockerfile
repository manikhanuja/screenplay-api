FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /app
 WORKDIR /app
 ADD requirements.txt /app/
 RUN pip install -r requirements.txt
 ADD . /app/
 
 RUN apt-get update && apt-get install -y wget
