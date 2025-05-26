# Purchase Order Notifier

A sample Python project that simulates a real-world queue system using RabbitMQ. It demonstrates the producer-consumer pattern for handling online store orders.

## ✅ Features
- Uses a custom virtual host and user in RabbitMQ
- Message durability (persistent exchange and queue)
- Clean separation of producer and consumer logic

## 🛠 Technologies
- Python 3
- RabbitMQ with Docker
- pika (RabbitMQ Python client)

## 🔧 Setup

1. Clone the repository:
```bash
git clone https://github.com/your-user/purchase-order-notifier.git
cd purchase-order-notifier
```

2. Run RabbitMQ:
```bash
docker-compose up -d
```

3. Set up virtual host `store` and user `storeuser` in the RabbitMQ UI.

4. Install dependencies:
```bash
pip install pika
```

5. Run producer:
```bash
python producer.py
```

6. Run consumer (in another terminal):
```bash
python consumer.py
```

## 📦 Queue Setup
- Virtual Host: `store`
- Exchange: `store.topic` (topic)
- Queue: `store.order.new`
- Routing Key: `order.created`

## 👥 Authors
- Stefan Jativa & Daniel Diaz
