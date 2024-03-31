import ssl
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe

class MQTTSubscriber:
    def __init__(self, hostnames, port=8883, credentials=None, topics=None):
        self.hostnames = hostnames
        self.port = port
        self.credentials = credentials
        self.topics = topics
        self.ssl_settings = ssl.create_default_context()
        self.ssl_settings.check_hostname = False

    def print_msg(self, message):
        decoded_payload = message.payload.decode("utf-8")
        print("%s : %s" % (message.topic, decoded_payload))

    def subscribe(self):
        for i, hostname in enumerate(self.hostnames):
            auth = {'username': self.credentials[i][0], 'password': self.credentials[i][1]} if self.credentials else None
            for topic in self.topics:
                subscribe.callback(self.print_msg, topic, hostname=hostname,
                                   port=self.port, auth=auth, tls=self.ssl_settings, protocol=paho.MQTTv311)

if __name__ == "__main__":
    hostnames = ["mqtt-s8trni.a01.euc1.aws.hivemq.cloud"]
    credentials = [("Bike1", "MQTTBike1"), ("Bike2", "MQTTBike2"), ("Bike3", "MQTTBike3"), ("Bike4", "MQTTBike4")]
    topics = ["mqtt/location/bike1", "mqtt/location/bike2", "mqtt/location/bike3","mqtt/location/bike4"]
    subscriber = MQTTSubscriber(hostnames=hostnames, credentials=credentials, topics=topics)
    subscriber.subscribe()