import paho.mqtt.publish as publish
import serial
import time
import sqlite3 as lite


MQTT_SERVER = "10.0.0.207"
MQTT_PATH_1 = "temperature"
MQTT_PATH_2 = "humidity"


ser = serial.Serial("/dev/cu.usbmodem14101",9600)
c = lite.connect('weather_data.db')
my_cursor = c.cursor()
my_cursor.execute('''CREATE TABLE IF NOT EXISTS SENSING (DAY TEXT NOT NULL, TIME TEXT NOT NULL, TEMPERATURE REAL NOT NULL, PRESSURE REAL NOT NULL)''')

while True:
    print("im in !!")
    line = ser.readline().strip()
    print("reading data")
    values = line.decode('ascii').split(',')
    a, b = [float(s) for s in values]
    print(a,b)
    print("obtained the values")
    
    day = time.strftime("%m/%d/%Y")
    time_1 = time.strftime("%H:%M:%S")
    print(day, time)
    
    parameters = (day, time_1, a, b)
    
    my_cursor.execute('''INSERT INTO SENSING (DAY, TIME, TEMPERATURE, PRESSURE) VALUES (?, ?, ?, ?)''',parameters)
    c.commit()
    print("successfully adding to database")
    publish.single(MQTT_PATH_1, a, hostname=MQTT_SERVER)
    publish.single(MQTT_PATH_2, b, hostname=MQTT_SERVER)
    
    my_cursor.execute('''SELECT * FROM SENSING''')
    print(my_cursor.fetchall())