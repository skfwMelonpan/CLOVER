#!/bin/sh

sudo /home/pi/sensor/GPS.py >> GPS.txt &
sudo /home/pi/sensor/MPU6050.py >> MPU.txt &
sudo /home/pi/sensor/HMC5883L.py >> HMC.txt &
