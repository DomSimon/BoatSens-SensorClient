import time,sys
import time
import requests

from pathlib import Path

sensor1 = '/sys/bus/w1/devices/28-02131390d8aa/w1_slave'
sensor2 = '/sys/bus/w1/devices/28-0213137cfeaa/w1_slave'

def readTempSensor(sensorName) :
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines

def readTempLines(sensorName) :
    lines = readTempSensor(sensorName)
    #print(lines)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(1)
        lines = readTempSensor()
    
 
        
    temperaturStr = lines[1].find('t=')
    # Ich überprüfe ob die Temperatur gefunden wurde.
    if temperaturStr != -1 :
        tempData = lines[1][temperaturStr+2:]
        tempCelsius = float(tempData) / 1000.0
        return tempCelsius

def sendAsJsonToServer(sensor_name, temp):
    

    newHeaders = {'Content-type': 'application/json'}
    response = requests.post('http://ec2-3-68-226-39.eu-central-1.compute.amazonaws.com:8080/postmap',
                         json={ "sensorname":sensor_name[20:35],
                                "sensorvalue":temp,
                                "sensortype":"temperature"
                                },
                         headers=newHeaders)
    print('JSON send')
    



while True :
    try:
        while True :
            temp1 = readTempLines(sensor1)
            print(time.strftime('%H:%M:%S') +" Sensor 1: " + str(temp1) + " °C")
            temp2 = readTempLines(sensor2)
            sendAsJsonToServer(sensor1, temp1)
            print(time.strftime('%H:%M:%S') +" Sensor 2: " + str(temp2) + " °C")
            sendAsJsonToServer(sensor2, temp2)
            time.sleep(60)

    except:
        print("exept opened wait 1 Minute")
        time.sleep(60)
        

        
    finally:
        print("try part is at finally")
        
