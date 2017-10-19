#!/bin/bash

sleep 10

cd /home/pi/Documents/CanSat_Payload_2017_1014/
touch error_output.log

# run a logging script
# in order to keep this script working properly,
# only have one of the lines below uncommented at a time...
# DOUBLE CHECK
# only one script should be uncommented at a time
# problems may arise if not

# run logging with camera
python log.py 2>&1 error_output.log

# run logging without camera
#python log_nocam.py 2>&1 error_output.log
