#!/bin/bash

# A script designed to compile and install neccessary dependencies for this software
# Depends on: bash, gcc, pip3
# By David Penkowoj, 2021/08/22

npm i &&
pip3 install spidev RPi.GPIO mfrc522 &&
gcc ./src/host/main.c -pthread -o rfidcws &&
echo "export PATH=$PATH:$(pwd)/rfidcws" >> "$HOME/.profile" &&
echo -e "\nSuccessfully installed RFIDCWS.\n" ||
echo -e "\nInstallation failed\n"
