FROM python:3
ENV PYTHONUNBUFFERED 1
#Tried with custom folder roots - got errors from docker. Invistigate later
RUN mkdir /composeexample
WORKDIR /composeexample
COPY requirements.txt /composeexample/
RUN pip install -r requirements.txt
COPY . /composeexample/