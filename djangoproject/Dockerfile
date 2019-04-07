FROM python:3
ENV PYTHONUNBUFFERED 1
#Tried with custom folder roots - got errors from docker. Invistigate later
RUN mkdir /djangoproject
WORKDIR /djangoproject
COPY requirements.txt /djangoproject/
RUN pip install -r requirements.txt
COPY . /djangoproject/
COPY . .