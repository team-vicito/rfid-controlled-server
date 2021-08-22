#!/bin/bash

# A script designed to compile and install neccessary dependencies for this software
# Depends on: bash, gcc, pip3
# By David Penkowoj, 2021/08/22

npm i &&
pip3 install spidev RPi.GPIO mfrc522 &&
gcc ./src/host/main.c -pthread -o rfid-controlled-server &&
echo "export PATH=$PATH:$(pwd)/rfid-controlled-server" >> "$HOME/.profile" &&
echo -e "\nSuccessfully installed rfid-controlled-server\n" ||
echo -e "\nInstallation failed\n"
