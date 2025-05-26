import pika
import json
import time

credentials = pika.PlainCredentials('storeuser', 'storepass')
params = pika.ConnectionParameters(
    host='rabbitmq',
    port=5672,
    virtual_host='store',
    credentials=credentials
)

for i in range(10):
    try:
        connection = pika.BlockingConnection(params)
        break
    except pika.exceptions.AMQPConnectionError:
        print("RabbitMQ no está listo, reintentando en 3 segundos...")
        time.sleep(3)
else:
    raise Exception("Could not connect to RabbitMQ after several attempts.")

channel = connection.channel()

exchange_name = 'store.topic'
queue_name = 'store.order.new'
routing_key = 'order.created'

channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

def handle_order(ch, method, properties, body):
    order = json.loads(body)
    print(f"Received new order: {order}")

channel.basic_consume(queue=queue_name, on_message_callback=handle_order, auto_ack=True)

print("Waiting for order messages...")
channel.start_consuming()
