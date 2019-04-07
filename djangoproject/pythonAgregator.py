import pika
import psycopg2
#import pyodbc
import numpy
import time
import json
import os
import sys
import datetime
import django
time.sleep(10)
from django.db import models
from djangoproject import settings
# from django.conf import settings
# from django.core.management import setup_environ


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# from django.conf import settings
# django.setup()

from table.models import valueTable


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()

channel.queue_declare(queue='samplequeue')
print('Connection')


print('WEll')

#


# arr = numpy.array([])

# How do we calculate?
# What if we got a later message?
# We calculate percentil on agregator's Time or recieved message one?
# We need to clear queue if it dropped
# So we need a buffer in out task

#Buffer with messages and calculate
#server id - value

#manage pi.migration
#manage pi.migrate
#how to orm django outside django

#react rest api

#datetime.datetime.now().time()
# t_end = time.time() + 60


# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='rabbit'))
# channel = connection.channel()

# channel.queue_declare(queue='samplequeue')
# print('Connection')

def put_in(val):
    print('value: '+str(val))
    new_value = valueTable(value=str(val), created_time = models.DateTimeField(auto_now_add=True))
    new_value.save()
    print('SENT')
    


def percentil(value):
   numpy.append(arr, value)
   if(time.time() ==t_end):       
       # insert_value(numpy.percentile(arr, 90))
        this.arr = numpy.array([])
        this.t_end+=60
        

def insert_value(record):
    sql = """INSERT INTO valueTable(_) VALUES(%s)""" #messageValues
    conn = None
    record_id=None
    try:
        params = config()        
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='postgres' password='password'")
        #conn = psycopg2.connect(**params)
        #db, err = gorm.Open("postgres", "host=postgres port=5432 user=postgres dbname=postgres password=password")
        cur = conn.cursor()
        cur.execute(sql, (record,))
        record_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print('RecordID:  '+str(record_id))


def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    message = json.loads(body)
    #print(message['value'])
   # while(time.time()<=t_end):
    #    percentil(int(message['value']))
    
    put_in(message['value'])
    #decoder
    #percentil(message['value'])
    #insert_value(body)
    print()
    # channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    #Connect to database and add value to it
    sys.stdout.flush()


channel.basic_consume(
    queue='samplequeue', on_message_callback=on_message, auto_ack=True)

channel.start_consuming()

# try:
# except KeyboardInterrupt:
    # channel.stop_consuming()
# connection.close()