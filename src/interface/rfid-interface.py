#!/usr/bin/env python3

# A simplified system for using RFID technology in combination with a webserver.
# Depends on: python3, PN532_I2C
# By David Penkowoj, 2021/06/08

import requests
import time
import sys

import light
import read

def main(reader):
  try: 
    print("Interface active. Waiting for RFID.")

    while True:
      uid = reader.read_passive_target(timeout=0.5)

      if uid is None:
        continue

      success(uid)

      time.sleep(1)
  except KeyboardInterrupt:
    sys.exit(0)

def success(uid):
  light.light()
  id = read.concat(uid)
  print("Found card with UID:", id)
  requests.post("http://localhost:1337/post", data = { "id": id })

if __name__ == "__main__":
  reader = read.setup()
  main(reader)
