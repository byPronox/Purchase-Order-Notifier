# Gestor de colas - Productor y Consumidor para Azure Service Bus

Se implemento un productor y un consumidor en Python para interactuar con una cola de Azure Service Bus llamada "cola-diaz" dentro del namespace "ServiceBusDiaz". El productor envía mensajes y el consumidor los recibe, utilizando políticas de acceso compartido separadas para "Send" y "Listen".

## Requisitos
- Automatic RabbitMQ setup with custom virtual host and user
- Durable exchanges and queues for message persistence
- Clean separation of producer and consumer logic
- Fully containerized with Docker Compose

## 🛠 Technologies
- Python 3
- Paquete azure-servicebus (pip install azure-servicebus)
- Namespace y cola configurados en Azure Service Bus

## Estructura
- producerAzure.py: Código del productor que envía mensajes a la cola.
- consumerAzure.py: Código del consumidor que recibe mensajes.
- config.ini: Archivo de configuración con las cadenas de conexión para   las políticas "Send" y "Listen".

## Portal Azure
- Namespace y Cola: Muestra el namespace "ServiceBusDiaz" y la cola "cola-diaz".

- Directivas de Acceso Compartido: Detalla las políticas "Send" y "Listen" configuradas para la cola "cola-diaz".

## Uso
- El archivo producerAzure.py envía un mensaje de prueba ("¡Hola desde el Productor!") a la cola "cola-diaz".

- El archivo consumerAzure.py escucha mensajes de la cola y los procesa, completándolos con receiver.complete_message(msg).

# Autor
Daniel Diaz