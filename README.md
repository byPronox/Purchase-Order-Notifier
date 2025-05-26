# Purchase Order Notifier

A sample Python project that simulates a real-world queue system using RabbitMQ. It demonstrates the producer-consumer pattern for handling online store orders.

## ✅ Features
- Automatic RabbitMQ setup with custom virtual host and user
- Durable exchanges and queues for message persistence
- Clean separation of producer and consumer logic
- Fully containerized with Docker Compose

## 🛠 Technologies
- Python 3
- RabbitMQ (Dockerized)
- pika (RabbitMQ Python client)
- Docker & Docker Compose

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-user/purchase-order-notifier.git
   cd purchase-order-notifier
   ```

2. **Start all services (RabbitMQ, Producer, Consumer):**
   ```bash
   docker-compose up --build
   ```

   - This will automatically:
     - Set up RabbitMQ with the virtual host `store` and user `storeuser`
     - Build and run the producer and consumer containers

3. **Check the logs:**
   - The producer will send a sample order event.
   - The consumer will receive and print the order event.

4. **RabbitMQ Management UI:**
   - Access at [http://localhost:15672](http://localhost:15672)
   - Login with:
     - **User:** `storeuser`
     - **Password:** `storepass`

## 📦 Queue Setup (automatic)
- **Virtual Host:** `store`
- **Exchange:** `store.topic` (type: topic)
- **Queue:** `store.order.new`
- **Routing Key:** `order.created`

## 👥 Authors
- Stefan Jativa & Daniel Diaz
