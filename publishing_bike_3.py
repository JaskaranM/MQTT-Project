import paho.mqtt.subscribe as subscribe
import ssl
import paho.mqtt.client as paho

def print_msg(message):
    decoded_payload = message.payload.decode("utf-8")
    print("%s : %s" % (message.topic, decoded_payload))

ssl_settings = ssl.create_default_context()
ssl_settings.check_hostname = False

auth = {'username': "Bike3", 'password': "MQTTBike3"}
subscribe.callback(print_msg, "mqtt/location/bike3", hostname="mqtt-s8trni.a01.euc1.aws.hivemq.cloud",
                   port=8883, auth=auth, tls=ssl_settings, protocol=paho.MQTTv311)
