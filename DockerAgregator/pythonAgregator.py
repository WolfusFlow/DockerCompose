import pika
import psycopg2
#import pyodbc
import numpy
import time
import json
import sys
import datetime
#from djangoproject.models import *
#from django.conf import settings

arr = numpy.array([])

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
t_end = time.time() + 60


def percentil(value):
   numpy.append(arr, value)
   if(time.time() ==t_end):       
       # insert_value(numpy.percentile(arr, 90))
        this.arr = numpy.array([])
        this.t_end+=60
        

def insert_value(record):
    sql = """INSERT INTO messageValues(_) VALUES(%s)""" #messageValues
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
    
    #decoder
    #percentil(message['value'])
    #insert_value(body)
    print()
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    #Connect to database and add value to it
    sys.stdout.flush()


connection = pika.BlockingConnection()
channel = connection.channel()
channel.basic_consume(on_message, 'samplequeue')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()