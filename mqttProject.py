# import required libraries

import paho.mqtt.client as mqtt
import time

# MQTT broker information

broker_address = "test.mosquitto.org"
broker_port = 1883

# Create MQTT client instance

client = mqtt.Client("bike_ID")

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
        
        # use of variables such as location/ latitiude etc will be useful 

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
