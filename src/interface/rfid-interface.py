#!/usr/bin/env python3

# A simplified system for using RFID technology in combination with a webserver.
# Depends on: python3, PN532_I2C
# By David Penkowoj, 2021/06/08

import requests
import board
import busio
import sys

from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

url = "http://localhost:1337/post"

def main(reader):
  try: 
    print("Interface active. Waiting for RFID.")

    while True:
      uid = reader.read_passive_target(timeout=0.5)

      if uid is None:
        continue

      print("Found card with UID:", concat(uid))

      map = {"id": id}
      requests.post(url, data = map)
  except KeyboardInterrupt:
    sys.exit(0)

def setup():
  i2c = busio.I2C(board.SCL, board.SDA)

  req_pin = DigitalInOut(board.D12)
  reset_pin = DigitalInOut(board.D6)
  pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
  
  ic, ver, rev, support = pn532.firmware_version
  print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
  
  pn532.SAM_configuration()

  return pn532

def concat(uid):
  string = ""
  for u in uid:
    string = string + str(u)

  return string

if __name__ == '__main__':
  reader = setup()
  main(reader)
