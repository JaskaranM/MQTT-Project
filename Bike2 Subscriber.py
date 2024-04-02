import paho.mqtt.subscribe as subscribe
import ssl
import sqlite3

#security aspect of the code
ssl_settings = ssl.create_default_context()
ssl_settings.check_hostname = False

#credentials to subscribe
auth = {'username': "Bike2", 'password': "MQTTBike2"}

#the function takes the message and outputs the coordinates
def process_message(client, userdata, message):
    decoded_payload = message.payload.decode("utf-8")
    print("Received message: %s" % decoded_payload)
    # takes the longitude and latitude out of the message
    latitude, longitude = map(float, decoded_payload.split(','))
    save_location_to_database(latitude, longitude)

#saves the location to the database
def save_location_to_database(latitude, longitude):
    # connects to the database and creates the pointer that allows for queries
    connection = sqlite3.connect('Database')
    cursor = connection.cursor()
    #because we have 4 separate files, we can set BikeID as a constant
    cursor.execute("UPDATE Bikes SET Latitude = ?, Longitude = ? WHERE BikeID = 'Bike2'", (latitude, longitude))
    connection.commit()

    print("Location data saved successfully")

    cursor.close()
    connection.close()

#subscribes to the topic
subscribe_topic = "mqtt/location/bike2"
subscribe.callback(process_message, subscribe_topic, hostname="mqtt-s8trni.a01.euc1.aws.hivemq.cloud",
                   port=8883, auth=auth, tls=ssl_settings)
