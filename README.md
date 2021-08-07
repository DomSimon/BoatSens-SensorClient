# BoatSens-SensorClient

This Code reads the output of 1-Wire Sensors on a RaspberryPi Zero-W and sends them as compatible JSON to a REST API.
A appropiate Backend is provided here: https://github.com/DomSimon/BoatSens-Backend

I recommend to run the Client as a Service on Raspberry Pi OS (Debian based).

Steps to activate the SensorClient as a Service

1.  Copy SensorClient.service to /lib/systemd/system/ and SensorClient.py to /home/root/
2.  Open the Terminal 
__ 3.  $ sudo systemctl daemon-reload
4.  $ sudo systemctl enable SensorClient.service
5.  $ sudo systemctl start SensorClient.service
6.  (optional) you can check if the service runs with $ sudo systemctl status SensorClient.service
