#!/bin/bash

# A script designed to compile and install neccessary dependencies for this software.
# Depends on: bash, gcc, pip3, npm
# By David Penkowoj, 2021/08/22

_prepareDependencies() {
  read -p "[ RFIDCWS ] Install dependencies with apt? [y/N] " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    echo -e "[ RFIDCWS ] Installing dependencies…\n" &&
    sudo apt install gcc python3-pip npm curl -y &&
    curl -fsSL https://deb.nodesource.com/setup_current.x | sudo bash - && sudo apt-get install -y nodejs &&
    echo -e "[ RFIDCWS ] Successfully installed dependencies\n" ||
    echo -e "[ RFIDCWS ] Failed installing dependencies\n"
  fi
}

_prepareRequirements() {
  echo -e "[ RFIDCWS ] Installing Node packages…\n" &&
  npm i &&
  echo -e "[ RFIDCWS ] Installing Python packages…\n" &&
  pip3 install spidev RPi.GPIO mfrc522 && 
  echo -e "\n[ RFIDCWS ] Requirements prepared." ||
  echo -e "\n[ RFIDCWS ] Requirements could not be prepared.\n"
}

_compile() {
  echo -e "[ RFIDCWS ] Compiling host software\n" &&
  gcc ./src/host/main.c -pthread -o rfidcws &&
  echo -e "\n[ RFIDCWS ] Successfully compiled RFIDCWS.\n" ||
  echo -e "\n[ RFIDCWS ] Compilation failed.\n"
}

case "$1" in
  "all")
    _prepareDependencies &&
    _prepareRequirements &&
    _compile
    ;;
  "host")
    _compile
    ;;
  "requirements")
    _prepareRequirements
    ;;
  "dependencies")
    _prepareDependencies
    ;;
  *)
    echo -e "[ RFIDCWS ] Unknown target. Please use 'all', 'host', 'requirements' or 'dependencies'.\n"
    ;;
esac