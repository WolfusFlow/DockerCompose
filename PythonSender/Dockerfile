FROM python:3

#WORKDIR /usr/src/app

RUN  pip install --no-cache-dir pika
# RUN  pip install --no-cache-dir puka

COPY . .  
#copy all files for fast docker up

#"./pythonSendPika.py   queueRabbit.py"
CMD [ "python", "./pythonSendPika.py" ] 