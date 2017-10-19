#!/bin/bash
# cleanup loggin stuff
# run this script to clear all files in ./Logging/

# remove existing log files
rm -rf "/home/pi/Documents/CanSat_Payload_2017_1014/Logging/*"

# remove error output files
rm -rf "/home/pi/Documents/CanSat_Payload_2017_1014/error*"
