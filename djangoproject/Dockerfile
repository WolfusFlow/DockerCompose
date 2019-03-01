FROM python:3
ENV PYTHONUNBUFFERED 1
#RUN mkdir /webdjango
RUN pip install djangorestframework
WORKDIR /djangoproject/
COPY requirements.txt /djangoproject/ 
RUN pip install -r requirements.txt
COPY . /djangoproject/