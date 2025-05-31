# Purchase Order ESB Notifier

A Python project that demonstrates a real-world producer-consumer scenario using Azure Service Bus as an Enterprise Service Bus (ESB). The producer sends purchase order events to a queue, and the consumer receives and processes them.

## ✅ Features
- Uses Azure Service Bus for decoupled messaging
- Producer and consumer separated in different modules
- Configuration file template provided (no secrets exposed)
- Ready for OOP refactoring

## 🛠 Technologies
- Python 3.11
- Azure Service Bus
- azure-servicebus Python SDK

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/byPronox/Purchase-Order-Notifier/tree/stefan
   cd purchase-order-notifier
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your connection:**
   - Copy `config/config_template.json` to `config/config.json`
   - Fill in your Azure Service Bus connection strings and queue name in `config.json`
   - **Do NOT commit your real `config.json` to GitHub!**

4. **Run the producer:**
   ```bash
   python producer/producer.py
   ```

5. **Run the consumer (in another terminal):**
   ```bash
   python consumer/consumer.py
   ```

## 📦 Configuration

- All sensitive connection data is stored in `config/config.json` (not tracked by git).
- Example template:
  ```json
  {
    "SERVICE_BUS_CONNECTION_STR_SEND": "Endpoint=sb://<your-namespace>.servicebus.windows.net/;SharedAccessKeyName=Send;SharedAccessKey=<your-key>;EntityPath=your-queue",
    "SERVICE_BUS_CONNECTION_STR_LISTEN": "Endpoint=sb://<your-namespace>.servicebus.windows.net/;SharedAccessKeyName=Listen;SharedAccessKey=<your-key>;EntityPath=your-queue",
    "QUEUE_NAME": "your-queue"
  }
  ```

## 🔒 Security

- The file `config/config.json` **must not be committed** to the repository.
- Add this line to your `.gitignore`:
  ```
  config/config.json
  ```

## 👥 Author
- Stefan Jativa
