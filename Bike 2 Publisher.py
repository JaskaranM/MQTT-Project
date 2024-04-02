import tkinter as tk
from tkinter import ttk
import geocoder
import paho.mqtt.publish as publish
import ssl

class LocationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bike1 Tracking App")

        # Defines the credentials and topic for Bike1
        self.bike_info = {"username": "Bike2", "password": "MQTTBike2", "topic": "mqtt/location/bike2"}

        # Creates and stores the tkinter frame with dimensions and location
        self.frame = ttk.Frame(self.root, padding="50")
        self.frame.grid(row=0, column=0)
        self.label = ttk.Label(self.frame, text="Tracking Bike2")
        self.label.grid(row=0, column=0)
        # Creates the button to start tracking
        self.button = ttk.Button(self.frame, text="Start Tracking", command=self.start_tracking)
        self.button.grid(row=1, column=0, pady=10)

    def start_tracking(self):
        # Calls the tracking function
        self.track_location()

    def track_location(self):
        # Get the current location
        location = geocoder.ip('me')
        if location.ok:
            latitude, longitude = location.latlng
            print(f"Current location for Bike1 - Latitude: {latitude}, Longitude: {longitude}")
            # Publish the new coordinates to the MQTT broker
            self.publish_coordinates_to_mqtt(latitude, longitude)
        else:
            print("Failed to retrieve current location.")

        # Schedule the next tracking after 30 seconds
        self.root.after(30000, self.track_location)

    def publish_coordinates_to_mqtt(self, latitude, longitude):
        ssl_settings = ssl.create_default_context()
        ssl_settings.check_hostname = False

        bike_info = self.bike_info
        auth = {'username': bike_info["username"], 'password': bike_info["password"]}

        publish_topic = bike_info["topic"]

        message = f"{latitude},{longitude}"

        publish.single(publish_topic, payload=message, hostname="mqtt-s8trni.a01.euc1.aws.hivemq.cloud",
                       port=8883, auth=auth, tls=ssl_settings)
        print("Coordinates published successfully.")

def main():
    root = tk.Tk()
    app = LocationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
