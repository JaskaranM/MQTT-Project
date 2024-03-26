import paho.mqtt.subscribe as subscribe
import ssl
import paho.mqtt.client as paho

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))

# Define SSL settings
ssl_settings = ssl.create_default_context()
ssl_settings.check_hostname = False

# Put in your cluster credentials and hostname
auth = {'username': "Bike1", 'password': "MQTTBike1"}
subscribe.callback(print_msg, "mqtt/location/bike1", hostname="da26e2370918479aba885bc54297a1d6.s1.eu.hivemq.cloud",
                   port=8883, auth=auth, tls=ssl_settings, protocol=paho.MQTTv311)
