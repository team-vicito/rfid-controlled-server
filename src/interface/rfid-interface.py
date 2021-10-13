#!/usr/bin/env python3

# A simplified system for using RFID technology in combination with a webserver.
# Depends on: python3, SimpleMFRC522, RPi
# By David Penkowoj, 2021/06/08

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import requests
import time
import sys

url = "http://localhost:1337/post"
reader = SimpleMFRC522()

def main():
  try: 
    print("Interface active. Waiting for RFID.")

    while True:
      try:
        id, data = reader.read()

        if id is None:
          continue

        map = {"id": id, "data": data}
        requests.post(url, data = map)
      except:
        print("Failed to read ID.")
      finally:
        time.sleep(0.5)
  except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)


if __name__ == '__main__':
  main()