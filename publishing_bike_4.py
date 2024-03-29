import paho.mqtt.subscribe as subscribe
import ssl
import paho.mqtt.client as paho

def print_msg(client, userdata, message):
    decoded_payload = message.payload.decode("utf-8")
    print("%s : %s" % (message.topic, decoded_payload))

ssl_settings = ssl.create_default_context()
ssl_settings.check_hostname = False

auth = {'username': "Bike4", 'password': "MQTTBike4"}
subscribe.callback(print_msg, "mqtt/location/bike4", hostname="bike-ex2s1d.a01.euc1.aws.hivemq.cloud",
                   port=8883, auth=auth, tls=ssl_settings, protocol=paho.MQTTv311)
