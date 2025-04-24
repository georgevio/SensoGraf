import time
import random
import paho.mqtt.client as mqtt

# MQTT Broker settings
BROKER_ADDRESS = 'localhost' # Replace with your broker's IP if not localhost
BROKER_PORT = 1883           # Default MQTT port
TOPIC = "iot_sensors/temperature"

# Callback for when the client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker")
    else:
        print(f"Connection failed with code {rc}")

def generate_temperature():
    """Simulate a temperature reading."""
    return round(random.uniform(20.0, 30.0), 2)  # Random temperature between 20°C and 30°C

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER_ADDRESS, BROKER_PORT)

    while True:
        temperature = generate_temperature()
        client.publish(TOPIC, temperature)
        print(f"Published temperature: {temperature}°C to topic: {TOPIC}")
        time.sleep(5)  # Publish every 5 seconds

if __name__ == "__main__":
    main()
