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
        self.clients = []

    def print_msg(self, message):
        decoded_payload = message.payload.decode("utf-8")
        print("%s : %s" % (message.topic, decoded_payload))

    def publish_msg(self, topic, message, client_index=0):
        if 0 <= client_index < len(self.clients):
            self.clients[client_index].publish(topic, message)
        else:
            print("Invalid client index.")

    def subscribe(self):
        for i, hostname in enumerate(self.hostnames):
            auth = {'username': self.credentials[i][0], 'password': self.credentials[i][1]} if self.credentials else None
            client = paho.Client()
            client.on_message = self.print_msg
            client.tls_set_context(context=self.ssl_settings)
            client.username_pw_set(username=auth['username'], password=auth['password']) if auth else None
            client.connect(hostname, port=self.port)
            client.loop_start()
            self.clients.append(client)
            for topic in self.topics:
                client.subscribe(topic)

if __name__ == "__main__":
    hostnames = ["bike-ex2s1d.a01.euc1.aws.hivemq.cloud"]
    credentials = [("Bike1", "MQTTBike1"), ("Bike2", "MQTTBike2"), ("Bike3", "MQTTBike3"), ("Bike4", "MQTTBike4")]
    topics = ["mqtt/location/bike1", "mqtt/location/bike2", "mqtt/location/bike3","mqtt/location/bike4"]
    subscriber = MQTTSubscriber(hostnames=hostnames, credentials=credentials, topics=topics)
    subscriber.subscribe()