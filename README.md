# BoatSens-SensorClient

This Code collects the output of 1-Wire Sensors on a RaspberryPi Zero-W and sends them as compatible JSON to a REST API.
A appropiate Backend is provided here: https://github.com/DomSimon/BoatSens-Backend

![raspisens](https://user-images.githubusercontent.com/63147491/128705369-766617a8-527b-4f29-88cb-065bd95f3be4.jpg)


I recommend to run the Client as a Service on Raspberry Pi OS (Debian based OS).
Services have the advantage, that they can be automatically restarted in cases like power loss or sensor errors.

## Steps to activate the SensorClient as a Service on a Linux based OS

Copy SensorClient.service to /lib/systemd/system/ and SensorClient.py to /home/root/ . 
Then run in Terminal:

1. ``` $ sudo systemctl daemon-reload ```
2. ``` $ sudo systemctl enable SensorClient.service ```
3. ``` $ sudo systemctl start SensorClient.service ```



(optional) You can check if the service runs with  
``` $ sudo systemctl status SensorClient.service ```
