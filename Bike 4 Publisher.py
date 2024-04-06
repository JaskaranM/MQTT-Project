import tkinter as tk
from tkinter import ttk
import geocoder
import paho.mqtt.publish as publish
import ssl

class LocationPublisher:
    def __init__(self, root):
        self.root = root
        self.root.title("Bike Tracker")
        self.bike_details = {"username": "Bike1", "password": "MQTTBike4", "topic": "mqtt/location/bike4"}
        #creates and stores the tkinter frame
        self.frame = ttk.Frame(self.root, padding="50")
        self.frame.grid(row=0, column=0)
        self.label = ttk.Label(self.frame, text="Track Bike4")
        self.label.grid(row=0, column=0)
        self.button = ttk.Button(self.frame, text="Start Tracking", command=self.start_tracking)
        self.button.grid(row=1, column=0, pady=10)

    def start_tracking(self):
        self.track_location()

    def track_location(self):
        #get the current location
        location = geocoder.ip('me')
        if location.ok:
            latitude, longitude = location.latlng
            print(f"Current location for Bike4 - Latitude: {latitude}, Longitude: {longitude}")
            #gives coordinates to the publishing function
            self.publish_coordinates_to_mqtt(latitude, longitude)
        else:
            print("Failed to retrieve current location.")
            #waits 30 seconds then publishes new coordinates
        self.root.after(30000, self.track_location)

    def publish_coordinates_to_mqtt(self, latitude, longitude):
        ssl_settings = ssl.create_default_context()
        ssl_settings.check_hostname = False
        bike_details = self.bike_details
        auth = {'username': bike_details["username"], 'password': bike_details["password"]}
        publish_topic = bike_details["topic"]
        message = f"{latitude},{longitude}"
        #publishes the message to the broker
        publish.single(publish_topic, payload=message, hostname="mqtt-s8trni.a01.euc1.aws.hivemq.cloud", port=8883, auth=auth, tls=ssl_settings)
        print("Coordinates published successfully.")

def main():
    root = tk.Tk()
    app = LocationPublisher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
