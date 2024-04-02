import tkinter as tk
from tkinter import ttk
import geocoder
import paho.mqtt.publish as publish
import ssl

class LocationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bike Tracking App")

        #defines the credentials and topic for each bike
        self.bikes_info = {
            "Bike1": {"username": "Bike1", "password": "MQTTBike1", "topic": "mqtt/location/bike1"},
            "Bike2": {"username": "Bike2", "password": "MQTTBike2", "topic": "mqtt/location/bike2"},
            "Bike3": {"username": "Bike3", "password": "MQTTBike3", "topic": "mqtt/location/bike3"},
            "Bike4": {"username": "Bike4", "password": "MQTTBike4", "topic": "mqtt/location/bike4"}
        }

        # creates and stores the tkinter frame with dimensions and location
        self.frame = ttk.Frame(self.root, padding="50")
        self.frame.grid(row=0, column=0)
        self.label = ttk.Label(self.frame, text="Select a bike:  ")
        self.label.grid(row=0, column=0)
        # creates the dropdown box that the user uses to choose an option
        self.drop_down_box = ttk.Combobox(self.frame, width=20, values=list(self.bikes_info.keys()))
        self.drop_down_box.grid(row=0, column=1)
        self.drop_down_box.current(0)
        # creates the button that will call the get_location function when pressed
        self.button = ttk.Button(self.frame, text="Start Tracking", command=self.start_tracking)
        self.button.grid(row=1, column=0, columnspan=2, pady=10)

    def start_tracking(self):
        #calls the tracking function
        self.track_location()

    def track_location(self):
        # Get the chosen bike
        bike_name = self.drop_down_box.get()
        # Get the current location
        location = geocoder.ip('me')
        if location.ok:
            latitude, longitude = location.latlng
            print(f"Current location - Latitude: {latitude}, Longitude: {longitude}")
            # Publish the new coordinates to the MQTT broker
            self.publish_coordinates_to_mqtt(bike_name, latitude, longitude)
        else:
            print("Failed to retrieve current location.")

        # Schedule the next tracking after 30 seconds
        self.root.after(30000, self.track_location)

    def publish_coordinates_to_mqtt(self, bike_name, latitude, longitude):
        ssl_settings = ssl.create_default_context()
        ssl_settings.check_hostname = False

        bike_info = self.bikes_info[bike_name]
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
