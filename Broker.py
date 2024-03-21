import paho.mqtt.client as mqtt

broker = 'iot.reyax.com'
port= 1883
topic = "api/request"
topic_sub = "api/notificatrion/37/#"

client_id = pass
username = pass
password = pass
device_id = pass


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
        
        else:
            print("Couldn't connect to broker, error code ", rc)
        
    
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client)
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}'from '{msg.topic}' topic")
    
    client.subscribe(topic_sub)
    client.on_message = on_message

def main():
    client = connect_mqtt
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    main()