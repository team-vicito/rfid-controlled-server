#!/usr/bin/env python3

# A simplified system for using RFID technology in combination with a webserver.
# Depends on: python3, SimpleMFRC522, RPi
# By David Penkowoj, 2021/06/08

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import requests
import time

url = 'localhost:1337/post'
reader = SimpleMFRC522()

def main():
  while True:
    try:
      time.sleep(0.5)
      id, data = reader.read()

      if id is not None:
        map = {"id": id, "data": data}
        requests.post(url, data = map)
    finally:
      GPIO.cleanup()

if __name__ == '__main__':
  main()
