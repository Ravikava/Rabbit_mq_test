import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='time_test')

def callback(ch, method, properties, body):
    print("Message Received : ", body)
    

channel.basic_consume(queue='time_test', on_message_callback=callback,auto_ack=True)

print(' [*] Waiting for messages. ')
channel.start_consuming()