from azure.servicebus import ServiceBusClient
import configparser

# Cargar configuración desde config.ini
config = configparser.ConfigParser()
config.read('config.ini')
connection_str = config['azure']['listen_connection_string']
queue_name = "cola-diaz"

# Crear un cliente de Service Bus
servicebus_client = ServiceBusClient.from_connection_string(connection_str)

# Recibir mensajes
with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name)
    with receiver:
        print("Escuchando mensajes...")
        for msg in receiver:
            print(f"Recibido: {str(msg)}")
            receiver.complete_message(msg)