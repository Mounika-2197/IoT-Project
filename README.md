# IoT-Project

EE-629 Raspberry Pi Web Server Environmental Sensing
Mounika Yakasiri 
Stevens Institute of Technology

Hi! Welcome to my Github!!

For this Project I have used an Arduino Nano 33 BLE Sense and Raspberry Pi 3B+, the data obtained from the arduino is temperature and humidity.

This project three different versions of obtaining Temperature and Humidity data from an Arduino Nano 33 BLE Sense
  1. Serially read data from the Arduino to RPi and display the real-time values to the webserver running on RPi.
  2. Send the Arduino data from any device that has internet access to RPi using MQTT Protocol.
  3. Sned the Arduino data from any device that has internet access directly to the webserver running on RPi using MQTT over Websockets.
  
  
1. Serially reading arduino data 
   The Serial_read.py performs this version of obtaining data. The Raspberry Pi behaves as a webserver, the web application is built using Flask micro webframework.
   The serially read data is displayed on the website at an interval of 1 minute.
   
2. MQTT protocol 
   broker.py performs displays the data obtained via MQTT protocol
   
3. MQTT over Websockets
   Publish_Websocket.py and Subscribe_Websocket.py performs MQTT over Websockets.
   Publish_Websocket.py is a python publisher, this code also serially reads the Arduino values. This is the program that runs on my MacBook.
   Subscrie_Websocket.html is a subscriber program running on my RPi, mosquitto broker also runs on the RPi. This program has the html code as well as the MQTT-subscriber code.
   Real-time data received over the websocket is updated at an interval of 1 minute.
  
