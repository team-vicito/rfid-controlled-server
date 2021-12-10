#!/usr/bin/env python3

# A script to print all information the system knows about a chip.
# Depends on: python3, 
# By David Penkowoj, 2021/12/07

import board
import busio
import yaml
import sys

from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

def main(reader):
  try: 
    print("Interface active. Waiting for RFID.")

    while True:
      uid = reader.read_passive_target(timeout=0.5)

      if uid is None:
        continue

      success(uid)

      return;
  except KeyboardInterrupt:
    sys.exit(0)

def success(uid):
  id = concat(uid)
  getInformation(id)
  print("Found card with UID:", id)

def getInformation(id):
    with open(f"../server/public/interactive-model-viewer/public/models/{id}.yml") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as error:
            print(f"Error! \n {error}")

def setup():
  i2c = busio.I2C(board.SCL, board.SDA)

  req_pin = DigitalInOut(board.D12)
  reset_pin = DigitalInOut(board.D6)
  pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
  
  _ic, ver, rev, _support = pn532.firmware_version
  print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
  
  pn532.SAM_configuration()

  return pn532

def concat(uid):
  string = ""
  for u in uid:
    string = string + str(u)

  return string

if __name__ == "__main__":
  reader = setup()
  main(reader)
