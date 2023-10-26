#!/usr/bin/python3
import serial
import time
import requests
from datetime import datetime
from urllib.parse import quote
import random

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)

temp = None
hum = None

while 1:
    input_str = ser.readline().decode("utf-8")
    if (input_str == ""):
        print("No Data")
    else :
        if ("Temperature:" in input_str):
            print("Température : " + input_str.split(" ")[1])
            temp = input_str.split(" ")[1]
        if ("Humidity:" in input_str):
            print("Humidité : " + input_str.split(" ")[1])
            hum = input_str.split(" ")[1]
        if (temp is not None and hum is not None):
            date = datetime.now()
            dateString = date.strftime("%Y-%m-%d %H:%M:%S")
            dateEncode = quote(dateString)
            tempEncode = quote(temp)
            humEncode = quote(hum)
            AQI = random.randint(0,150)
            AQIEncode = quote(str(AQI))
            url = f"https://greenairapi.onrender.com/Mesure?Temperature={tempEncode}&Humidite={humEncode}&AQI={AQIEncode}&DateHeure={dateEncode}&ParkId=1"
            print(url)
            print("Envoie en cours")
            
            response = requests.post(url)
            time.sleep(30)
            if (response.status_code == 200):
                print("Données envoyées")
            else:
                print(f"Echec de la requête avec le code : {response.status_code}")
            hum = None
            temp = None
            
    time.sleep(30)