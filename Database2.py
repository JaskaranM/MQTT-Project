import sqlite3

# Connect to the SQLite database file
connection = sqlite3.connect("MQTT_messages.db")
cursor = connection.cursor()

# Create the MQTTMessages table if it doesn't exist
create_mqtt_messages_table = """
CREATE TABLE IF NOT EXISTS MQTTMessages (
    message_ID INTEGER PRIMARY KEY,
    bike_ID INTEGER,
    topic TEXT,
    payload TEXT,
    timestamp TEXT,
    longitute TEXT
)
"""
cursor.execute(create_mqtt_messages_table)


cursor.close()
connection.commit()


with connection:
    cursor = connection.cursor()
    rows = cursor.execute("SELECT bike_ID, location FROM MQTTMessages").fetchall()
    print(rows)