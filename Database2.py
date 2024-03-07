import sqlite3


connection = sqlite3.connect("MQTT_messages.db")
cursor = connection.cursor()


create_mqtt_messages_table = """
CREATE TABLE IF NOT EXISTS MQTTMessages (
    message_id INTEGER PRIMARY KEY,
    bike_id INTEGER,
    timestamp TEXT,
    longitude TEXT,
    latitude TEXT
)
"""
cursor.execute(create_mqtt_messages_table)


cursor.close()
connection.commit()


with connection:
    cursor = connection.cursor()
    rows = cursor.execute("SELECT bike_id, longitude, latitude FROM MQTTMessages").fetchall()
    print(rows)