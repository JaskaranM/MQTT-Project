import paho.mqtt.subscribe as subscribe
import ssl
import sqlite3

# Security aspect of the code
ssl_settings = ssl.create_default_context()
ssl_settings.check_hostname = False

# Define function to process messages and save location to the database
def process_message(client, userdata, message):
    decoded_payload = message.payload.decode("utf-8")
    print("Received message: %s" % decoded_payload)
    bike_id = userdata  # Extract bike_id from userdata
    # Takes the longitude and latitude out of the message
    latitude, longitude = map(float, decoded_payload.split(','))
    save_location_to_database(bike_id, latitude, longitude)

# Save location to the database
def save_location_to_database(bike_id, latitude, longitude):
    # Connects to the database and creates the pointer that allows for queries
    connection = sqlite3.connect('Database')
    cursor = connection.cursor()
    # Update location based on bike_id
    cursor.execute("UPDATE Bikes SET Latitude = ?, Longitude = ? WHERE BikeID = ?", (latitude, longitude, bike_id))
    connection.commit()

    print("Location data saved successfully for BikeID:", bike_id)

    cursor.close()
    connection.close()

# Define MQTT subscription credentials and topics for each bike
subscriptions = [
    {"username": "Bike1", "password": "MQTTBike1", "topic": "mqtt/location/bike1"},
    {"username": "Bike2", "password": "MQTTBike2", "topic": "mqtt/location/bike2"},
    {"username": "Bike3", "password": "MQTTBike3", "topic": "mqtt/location/bike3"},
    {"username": "Bike4", "password": "MQTTBike4", "topic": "mqtt/location/bike4"}
]

# Subscribe to MQTT topics for each bike
for sub in subscriptions:
    subscribe.callback(
        process_message, 
        sub["topic"], 
        hostname="mqtt-s8trni.a01.euc1.aws.hivemq.cloud",
        port=8883, 
        auth=sub, 
        tls=ssl_settings,
        userdata=sub["username"]  # Pass bike_id as userdata
    )
