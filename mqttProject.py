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
        client.subscribe("status/location/bikeID")  # Subscribe to the desired topic(s)
    else:
        print("Connection failed. RC: " +str(rc))

def on_message(client, userdata, msg):
    
    print(msg.topic+" "+str(msg.payload))

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

# potential functions:

def userReg():

    pass

def locTracking():

    pass

# potential data types (include in documentation)

bikeData = 0 # bike ID

userData = 1 # can use a database here

locData = 2 #including latitude, longitude, timestamp