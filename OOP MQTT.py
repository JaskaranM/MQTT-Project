import paho.mqtt.client as mqtt
import time
import json

class MQTTClient:
    def __init__(self, client_id, broker_address, broker_port):
        self.client_id = client_id
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.client = mqtt.Client(self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker!")
            client.subscribe("status/location/") + self.client_id #Subscribe to the desired topics
        else:
            print("Connection failed. RC: " + str(rc))

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def connect(self):
        self.client.connect(self.broker_address, self.broker_port)
    
    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

    def disconnect(self):
        self.client.disconnect()

class Updater:
    def __init__(self, update_interval):
        self.update_interval = update_interval
        self.last_update_time = time.time()

    def update(self):
        current_time = time.time()
        if current_time - self.last_update_time >= self.update_interval:
            print("Updater class updated.")
            self.last_update_time = current_time

class Telemetry(Updater):
    def __init__(self, time, distance, update_intervals, distance_threshold):
        super().__init__(update_intervals)
        self.time = time
        self.distance = distance
        self.distance_threshold = distance_threshold
    
    def update(self):
        super().update()

        if self.distance >= self.distance_threshold:
            print("Distacnce threshold reached. Updating Updater")
            super().update()



if __name__ == "__main__":
    client = MQTTClient("bike_ID", "test.mosquitto.org", 1833)
    client.connect()
    client.start()
    telemetry_data = Telemetry("10:30", 15)
    print(telemetry_data)