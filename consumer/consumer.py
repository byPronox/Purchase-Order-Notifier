import json
from azure.servicebus import ServiceBusClient
import os

with open(os.path.join(os.path.dirname(__file__), '../config/config.json')) as f:
    config = json.load(f)

connection_str = config["SERVICE_BUS_CONNECTION_STR_LISTEN"]
queue_name = config["QUEUE_NAME"]

with ServiceBusClient.from_connection_string(connection_str) as client:
    receiver = client.get_queue_receiver(queue_name)
    with receiver:
        for msg in receiver:
            order = json.loads(str(msg))
            print("Received order:", order)
            receiver.complete_message(msg)