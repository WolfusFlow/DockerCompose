FROM python:3

#WORKDIR /usr/src/app

RUN  pip install --no-cache-dir pika
RUN  pip install --no-cache-dir psycopg2
RUN  pip install --no-cache-dir config
RUN  pip install --no-cache-dir numpy
# RUN  pip install --no-cache-dir puka

COPY . .

#"./pythonSendPika.py   pythonAgregator.py"
CMD [ "python", "./pythonAgregator.py" ] 