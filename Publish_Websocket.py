import paho.mqtt.client as paho #mqtt library
import os
import json
import time
from datetime import datetime
import serial


broker="10.0.0.207" #host name , Replace with your IP address.
topic="test";
port=1883 #MQTT data listening port
ACCESS_TOKEN='M7OFDCmemyKoi461BJ4j'



ser = serial.Serial("/dev/cu.usbmodem14101",9600)

def on_publish(client,userdata,result): #create function for callback
  print("published data is : ")
  pass

client1= paho.Client("control1") #create client object
client1.on_publish = on_publish #assign function to callback
client1.username_pw_set(ACCESS_TOKEN) #access token from thingsboard device
client1.connect(broker,port,keepalive=60) #establishing connection

while True:
   print("im in !!")
   line = ser.readline().strip()
   print("reading data")
   values = line.decode('ascii').split(',')
   a, b = [float(s) for s in values]
   temp = str(a)
   humidity = str(b)
   print(a,b)
   print("obtained the values")

   day = time.strftime("%m/%d/%Y")
   time_1 = time.strftime("%H:%M:%S")
   print(day, time)

   parameters = (day, time_1, a, b)

    
   print("successfully adding to database")
   #publish.single(MQTT_PATH_1, a, hostname=MQTT_SERVER)
   #publish.single(MQTT_PATH_2, b, hostname=MQTT_SERVER)


   payload = "Current Humidity is: " + humidity;
   payload += ",";
   payload += '  ';
   payload += "Current Temperature is: " + temp;
   
   
  
   ret= client1.publish(topic,payload) #topic name is test
   print(payload);
   print("Please check data on your Subscriber Code \n")
   time.sleep(5)
    
    