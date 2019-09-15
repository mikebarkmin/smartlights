#!/bin/bash
scp -rp ../python pi@$1:/home/pi/Server
ssh pi@$1 sudo mv /home/pi/Server/gateway.service /lib/systemd/system/
ssh pi@$1 sudo systemctl daemon-reload
ssh pi@$1 sudo systemctl enable gateway.service
ssh pi@$1 sudo systemctl start gateway.service

