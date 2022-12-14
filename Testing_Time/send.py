import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='time_test')

def time_test(n):
    message=str(n*25)
    channel.basic_publish(exchange='',routing_key='time_test',body=message)
    print(f'\n\n -- {message} -- \n\n')

n = 1
while n < 10:
    time_test(n)
    time.sleep(10)
    n += 1
    