from azure.servicebus import ServiceBusClient, ServiceBusMessage
import configparser

# Cargar configuración desde config.ini
config = configparser.ConfigParser()
config.read('config.ini')
connection_str = config['azure']['send_connection_string']
queue_name = "cola-diaz"

# Crear un cliente de Service Bus
servicebus_client = ServiceBusClient.from_connection_string(connection_str)

# Enviar un mensaje
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name)
    with sender:
        message = ServiceBusMessage("¡Hola desde el Productor de Daniel Diaz!")
        sender.send_messages(message)
        print("Mensaje enviado con éxito.")