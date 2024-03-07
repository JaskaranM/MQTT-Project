import paho.mqtt.client as mqtt
import time
import json

class OwnTracksHandler:
    def __init__(self, broker_address, broker_port, owntracks_topic):
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.owntracks_topic = owntracks_topic

        self.client = mqtt.Client("BikeTracker")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def connect(self):
        self.client.connect(self.broker_address, self.broker_port)
        self.client.subscribe("owntracks/+/+")
    
    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to OwnTracks broker! ")
            client.subscribe(self.owntracks_topic)
        else:
            print("Connection to OwnTracks broker failed! ")

    def on_message(self, client, userdata, msg):
      payload = json.loads(msg.payload.decode())
      if 'lat' in payload and 'lon' in payload:
          print("Recieved OwnTracks location update: ", payload)

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
    owntracks_handler = OwnTracksHandler("test.mosquitto.org", 1833, "owntracks/+/+")
    owntracks_handler.connect()
    owntracks_handler.start()
    telemetry_data = Telemetry("10:30", 15, 60, 20)
    print(telemetry_data)