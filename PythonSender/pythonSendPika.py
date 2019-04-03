import pika
import random
import time
import sys
import json
import os
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit')) #write as 127 and port?  https://127.0.0.1 
channel = connection.channel()
channel.queue_declare(queue='samplequeue')

min_char = 0;
max_char = 128000;

r = random.randint(min_char,max_char);

def changeNumber(r):
    r = r+random.randint(-4000, 4000)
    if(r>=max_char):
        return max_char
    if(r<=min_char):
        return min_char
    return r   #add more conditions in future

def sendMessage(value):     
    #  #think of how to get current compose id of process   
#print(os.environ.get('SERVERNAME'))
#print(os.environ["SERVERNAME"])
#print(os.getenv('${SERVERNAME}'))
    print(sys.argv)
    print(os.getenv('SERVERNAME')) # Somehow to get an id of process? but if we stop it will be different
    #we need a constant id param of it?

    channel.basic_publish(exchange='',
                      routing_key='samplequeue', #key = samplekey 
                      body=json.dumps({'type': 'ram', 'value': value, 'datetime': datetime.datetime.now().isoformat(), 'server_id': 1}))
    print('current Value :\n'+str(json.dumps({'type': 'ram', 'value': value, 'datetime': datetime.datetime.now().isoformat(), 'server_id': 1})))
    

while True:
    r = changeNumber(r)
    sendMessage(r)
    sys.stdout.flush()
    time.sleep(1)

connection.close()