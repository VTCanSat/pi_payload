#!/bin/bash

# really annoying, but just copy this line and it should work
# not sure why the command won't work in a script

# kills the script by pid
sudo kill $(ps aux | grep "log*.py" | awk '{print $2}')
