import paho.mqtt.client as mqtt
import sqlite3 as lite
import sys
from flask import Flask

 
MQTT_SERVER = "localhost"
MQTT_PATH_1 = "temperature"
MQTT_PATH_2 = "humidity"

 
# The callback for when the client receives a CONNACK response from the server.

app = Flask(__name__)
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH_1)
    client.subscribe(MQTT_PATH_2)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    print(msg.topic+" "+str(msg.payload))
    message = msg.payload()
    web_server(message)
    print(message)
    
    # more callbacks, etc
@app.route("/")
def web_server(message):
    return render_template("main.html",message)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.web_server = web_server 

         
    
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

     
     
client.loop_forever()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
