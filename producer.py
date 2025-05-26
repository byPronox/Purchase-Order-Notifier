import pika
import json
import time
from datetime import datetime, timezone

order_data = {
    "order_id": 101,
    "user": "Stefan",
    "total": 149.99,
    "created_at": datetime.now(timezone.utc).isoformat()
}

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
    raise Exception("No se pudo conectar a RabbitMQ después de varios intentos.")

channel = connection.channel()

exchange_name = 'store.topic'
routing_key = 'order.created'

channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

channel.basic_publish(
    exchange=exchange_name,
    routing_key=routing_key,
    body=json.dumps(order_data)
)

print("Order event sent:", order_data)
connection.close()