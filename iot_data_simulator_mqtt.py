import paho.mqtt.client as mqtt
import time
import json
import random

# MQTT broker configuration
MQTT_BROKER = "mqtt-broker"  # Use the container name or localhost
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensors"

# The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Failed to connect, return code {rc}")

# Simulate sensor data
def generate_sensor_data():
    return {
        "location": {
            "balcony": {
                "temperature": round(random.uniform(15, 25), 2),
                "pressure": round(random.uniform(1000, 1020), 2)
            },
            "house": {
                "temperature": round(random.uniform(20, 30), 2),
                "pressure": round(random.uniform(1010, 1030), 2)
            }
        }
    }

# Create an MQTT client instance
client = mqtt.Client()

# Set callbacks
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the network loop in a separate thread
client.loop_start()

# Publish data in a loop
try:
    while True:
        sensor_data = generate_sensor_data()
        client.publish(MQTT_TOPIC, json.dumps(sensor_data))
        print(f"Published: {sensor_data}")
        time.sleep(5)  # Publish every 5 seconds
except KeyboardInterrupt:
    print("Stopping simulator...")
finally:
    client.loop_stop()
    client.disconnect()