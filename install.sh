#!/bin/bash

# A script designed to compile and install neccessary dependencies for this software
# Depends on: bash, gcc, pip3
# By David Penkowoj, 2021/08/22

_enableSPI() {
    if ! grep "dtparam=spi=on" /boot/config.txt; then
        echo "dtparam=spi=on" >> "/boot/config.txt"
    fi
}

_prepareRequirements() {
    npm i &&
    _enableSPI && 
    pip3 install spidev RPi.GPIO mfrc522
}

_compile() {
    _prepareRequirements &&
    gcc ./src/host/main.c -pthread -o rfidcws
}

_compile &&
echo -e "\nSuccessfully compiled RFIDCWS.\n" ||
echo -e "\nInstallation failed\n"
