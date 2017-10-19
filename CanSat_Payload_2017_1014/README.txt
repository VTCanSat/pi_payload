Operation for logging on this pi:

1)
On startup, kill the currently running log process by copying the command in the kill_process.sh file. It is shown here:

sudo kill $(ps aux | grep "log*.py" | awk '{print $2}')

2)
Check any files you would like to check, optionally copy them to another directory to save them

3)
Then, if you would like to cleanup the Logging directory, run cleanup.sh by using this command:

sudo sh cleanup.sh

If the script does not work, run the lines in the file.

4)
Optionally, you can change the script from logging images or only logging BMP180 sensor readings by modifying the script in /home/pi/ called log_launch.sh

Simply uncomment the desired script and comment out the old script

5)
Shutdown the pi correctly.

6)
On startup, logging will begin after about 60 seconds.


Other Notes:
I measured that the lens of the camera should be extended about 2.85 cm from the edge of the pi's enclosure. This is very rough, but it will increase the likelihood that the images are in focus.

