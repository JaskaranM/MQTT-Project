import paho.mqtt.subscribe as subscribe
import ssl
import sqlite3

#security aspect of the code
ssl_settings = ssl.create_default_context()
ssl_settings.check_hostname = False

#decodes the message
def decode_message(client, userdata, message):
    decoded_payload = message.payload.decode("utf-8")
    print("Received message: %s" % decoded_payload)
    bike_id = userdata
    latitude, longitude = map(float, decoded_payload.split(','))
    save_to_database(bike_id, latitude, longitude)


def save_to_database(bike_id, latitude, longitude):
    #connects to the database and creates the pointer that allows for queries
    connection = sqlite3.connect('Database')
    cursor = connection.cursor()
    #updates row based on BikeID
    cursor.execute("UPDATE Bikes SET Latitude = ?, Longitude = ? WHERE BikeID = ?", (latitude, longitude, bike_id))
    connection.commit()

    print("Location data saved successfully for BikeID:", bike_id)

    cursor.close()
    connection.close()

#the credentials for each bike
subscriptions = [
    {"username": "Bike1", "password": "MQTTBike1", "topic": "mqtt/location/bike1"},
    {"username": "Bike2", "password": "MQTTBike2", "topic": "mqtt/location/bike2"},
    {"username": "Bike3", "password": "MQTTBike3", "topic": "mqtt/location/bike3"},
    {"username": "Bike4", "password": "MQTTBike4", "topic": "mqtt/location/bike4"}
]

#subscribes to topics
for sub in subscriptions:
    subscribe.callback(
        decode_message, 
        sub["topic"], 
        hostname="mqtt-s8trni.a01.euc1.aws.hivemq.cloud",
        port=8883, 
        auth=sub, 
        tls=ssl_settings,
        userdata=sub["username"]
    )
