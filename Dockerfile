FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY iot_data_simulator_mqtt.py .

CMD ["python", "iot_data_simulator_mqtt.py"]