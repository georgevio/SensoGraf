import paho.mqtt.client as mqtt

# MQTT Broker settings
BROKER_ADDRESS = "localhost"  # Replace with your broker's IP if not localhost
BROKER_PORT = 1883           # Default MQTT port
TOPIC = "iot_sensors/temperature"

# Callback for when the client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker")
        client.subscribe(TOPIC)  # Subscribe to the topic upon successful connection
        print(f"Subscribed to topic(s): {TOPIC}")
    else:
        print(f"Connection failed with code {rc}")

# Callback for when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}°C from topic: {message.topic}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
