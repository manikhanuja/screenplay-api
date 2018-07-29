FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /app
 WORKDIR /app
 ADD requirements.txt /app/
 RUN pip install -r requirements.txt
 ADD . /app/
 
 RUN apt-get update && apt-get install -y wget

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz