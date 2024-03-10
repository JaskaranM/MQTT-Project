# import required libraries

import paho.mqtt.client as mqtt
import time
import json
import sqlite3

# MQTT broker information

broker_address = "test.mosquitto.org"
broker_port = 1883

# Create MQTT client instance

client = mqtt.Client("bike_ID")

# SQLite database initialization

db_test_file = "bike_data.db"
connectTo = sqlite3.connect(db_test_file) # name of Aman's file...
c = connectTo.cursor()

# Create table if it doesn't already exist

c.execute('''CREATE TABLE IF NOT EXISTS bike_location
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              bike_id TEXT,
              latitude REAL,
              longitude REAL,
              timestamp INTEGER)''')

# Commit changes and close the database connection

connectTo.commit()

# define a callback function on_message to handle messages received on subscribed topics.

def on_connect(client, userdata, flags, rc):
    
    if rc == 0:
        print("Connected to broker")
        client.subscribe("owntracks/GS/GS")  # Subscribe to the desired topic(s) - Subscribe to the OwnTracks topic where location updates are published
    else:
        print("Connection failed. RC: " +str(rc))

def on_message(client, userdata, msg):
    
    print(msg.topic+" "+str(msg.payload))

def handle_example_message(payload):
    # Parse the message payload and execute actions based on its content
    
    data = json.loads(payload)
    action = data.get("action") # stop bike/ continue after stopping/ stop using bike....
    if action == "do_something":
        # Execute the appropriate action
        print("Doing something...") # print message to client updating of the status of bike...

            # Publish the message to the specified topic
        publish.single("owntracks/GS/GS", json.dumps(action), hostname="test.mosquitto.org", port=1883)
        print("Message published:", action)
        
        time.sleep(10)  # Wait for 10 seconds before publishing the next message # can be changed

# Call the function to publish example messages
publish_example_messages()
        
        # use of variables such as location/ latitiude etc will be useful 

    # Insert data into SQLite database
    c.execute('''INSERT INTO bike_location (bike_id, latitude, longitude, timestamp) 
                 VALUES (?, ?, ?, ?)''', (bike_id, latitude, longitude, timestamp)) # whatever the fields are...
    connectTo.commit()  # Commit changes to the database

# set up MQTT client

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# loop to maintain connection and process messages

#client.loop_forever()

# Start the loop/ stop
client.loop_start()
client.loop_stop()
client.disconnect() #maybe use a try/except to handle this or allow it to loop forever until declared

# potential functions: // may have to be classes now for OOP marks 

def userReg():

    pass

def locTracking():

    pass

def update_location(locData):
    
    pass

# potential data types (include in documentation)

bikeData = 0 # bike ID

userData = 1 # can use a database here

locData = 2 #including latitude, longitude, timestamp

# also consider using a database - maybe SQLite....
# keep it relatively simple and just let it store and update user info, location... 

# need to establish connection between tkinter GUI, subscriber script for MQTT, and database

# implement the GUI components - necessary buttons etc...(basically just finish frontend)

# Add MQTT Subscriber Functionality - incorporate functionality in Jas' Tkinter application to subscribe to 
# MQTT messages. we can use the paho.mqtt.client library within the Tkinter application when merged/ declared
# to establish a connection to the MQTT broker and receive messages.

# Update GUI with MQTT Data - implement logic to update the Tkinter GUI with the data received from MQTT 
# messages. For example, if we receive location data for bikes, we should update relevant labels or display 
# the data in a list or table within your Tkinter application and update the database as needs be.

# Integrate SQLite database interaction - use the sqlite3 library to interact with the SQLite database.

# Update GUI with database data - somehow...

# example functions could include:

class BikeTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Bike Tracker")


    def query_database(self):
        # Query SQLite database for relevant data
        self.c.execute("SELECT * FROM bike_location")
        data = self.c.fetchall()
        # Process and update GUI with database data

