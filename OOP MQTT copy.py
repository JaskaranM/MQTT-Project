import ssl
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe

class MQTTSubscriber:
    def __init__(self, hostname, port=8883, username=None, password=None, topic="#"):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.topic = topic
        self.ssl_settings = ssl.create_default_context()
        self.ssl_settings.check_hostname = False

    def print_msg(self, client, userdata, message):
        print("%s : %s" % (message.topic, message.payload))

    def subscribe(self):
        auth = {'username': self.username, 'password': self.password} if self.username and self.password else None
        subscribe.callback(self.print_msg, self.topic, hostname=self.hostname,
                           port=self.port, auth=auth, tls=self.ssl_settings, protocol=paho.MQTTv311)

if __name__ == "__main__":
    subscriber = MQTTSubscriber(hostname="f3ad52f868214341bbbcfa09eb9cacfa.s1.eu.hivemq.cloud",
                                username="Bike1", password="MQTTBike1")
    subscriber.subscribe()
