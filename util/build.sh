#!/bin/bash

# A script designed to compile and build the software.
# Depends on: bash, gcc, pip3, npm
# By David Penkowoj, 2021/08/22

_buildHost() {
  echo -e "[ RFIDCWS ] Compiling host software\n" &&
  gcc ./src/host/main.c -pthread -o rfidcws &&
  echo -e "\n[ RFIDCWS ] Successfully compiled RFIDCWS.\n" ||
  echo -e "\n[ RFIDCWS ] Compilation failed.\n"
}

_buildViewer() {
  echo -e "[ RFIDCWS ] Building web client\n" &&
  cd ../src/server/public/interactive-model-viewer/ &&
  npm run pack &&
  echo -e "\n[ RFIDCWS ] Successfully built web client.\n" ||
  echo -e "\n[ RFIDCWS ] Build failed.\n"
}

case "$1" in
  "all")
    _buildHost
    _buildViewer
    ;;
  "host")
    _buildHost
    ;;
  "viewer")
    _buildViewer
    ;;
  *)
    echo -e "[ RFIDCWS ] Unknown target. Please use 'all', 'host'  or 'viewer'.\n"
    ;;
esac