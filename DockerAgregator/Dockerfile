FROM python:3

#WORKDIR /usr/src/app

RUN  pip install --no-cache-dir pika
RUN  pip install --no-cache-dir psycopg2-binary
RUN  pip install --no-cache-dir config
RUN  pip install --no-cache-dir numpy
RUN  pip install --no-cache-dir django
# RUN  pip install --no-cache-dir puka

# COPY /djangoproject/ .
# COPY ~/djangoproject/table/models.py ./ormDb
# WORKDIR /DockerAgregator

# COPY . DockerAgregator
COPY . .

# COPY . /DockerAgregator/

#"./pythonSendPika.py   pythonAgregator.py"

CMD [ "python", "./DockerAgregator/pythonAgregator.py" ] 
# CMD [ "python", "./manage.py", "sql", "ormDb" ]