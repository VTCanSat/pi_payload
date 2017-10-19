# Sky Hoffert
# Oct 14, 2017
# Version 1
# log.py
# Log BMP180 and pi-camera data to ./Logging/ director

import Adafruit_BMP.BMP085 as BMP085
import picamera
import sys
import os
from time import gmtime, strftime
import time

# handle args
date_time = strftime('%Y-%m-%d-%H:%M:%S', gmtime())
os.system('mkdir Logging/{}'.format(date_time))

# create sensors
bmp180 = BMP085.BMP085()
camera = picamera.PiCamera()

temperature = 0
pressure = 0
altitude = 0

# create log file
log_file = open('Logging/{}/log_file.csv'.format(date_time), 'w', 0)

while (1):
    # read bmp
    temperature = bmp180.read_temperature()
    pressure = bmp180.read_pressure()
    altitude = bmp180.read_altitude()

    # read the current system time
    time_now = ((int)(time.time() * 1000))

    # write log to file
    log_file.write('{},'.format(time_now))
    log_file.write('{0:0.2f},'.format(temperature))
    log_file.write('{0:0.2f},'.format(pressure))
    log_file.write('{0:0.2f},'.format(altitude))
    log_file.write('\n')

    # take image
    camera.capture('Logging/{}/{}.jpg'.format(date_time, time_now))

# clearnup
log_file.close()

exit(0)
