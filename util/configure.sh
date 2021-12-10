#!/bin/bash

# A script designed to configure and install neccessary dependencies for this software.
# Depends on: bash, gcc, pip3, npm
# By David Penkowoj, 2021/08/22

_preparePackages() {
  read -p "[ RFIDCWS ] Install required packages with apt? [y/N] " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    echo -e "[ RFIDCWS ] Installing packages…\n" &&
    sudo apt install gcc python3-pip npm curl -y &&
    curl -fsSL https://deb.nodesource.com/setup_current.x | sudo bash - && sudo apt-get install -y nodejs &&
    echo -e "[ RFIDCWS ] Successfully installed packages\n" ||
    echo -e "[ RFIDCWS ] Failed installing packages\n"
  fi
}

# TODO: Check dependencies (python)
_prepareDependencies() {
  echo -e "[ RFIDCWS ] Installing Node dependencies…\n" &&
  npm i &&
  echo -e "[ RFIDCWS ] Installing Python dependencies…\n" &&
  pip3 install spidev RPi.GPIO mfrc522 pyyaml board busio && 
  echo -e "\n[ RFIDCWS ] Dependencies configured successfully." ||
  echo -e "\n[ RFIDCWS ] Dependencies could not be configured.\n"
}

case "$1" in
  "all")
    _preparePackages
    _prepareDependencies
    ;;
  "packages")
    _preparePackages
    ;;
  "dependencies")
    _prepareDependencies
    ;;
  *)
    echo -e "[ RFIDCWS ] Unknown target. Please use 'all', 'packages' or 'dependencies'.\n"
    ;;
esac