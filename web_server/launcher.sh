#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back homecd /


cd home/pi/web_server/
sudo python gpio_ctrl.py
cd /
