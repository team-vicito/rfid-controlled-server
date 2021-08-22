#!/usr/bin/env python3

# A simplified system for using RFID technology in combination with a webserver.
# Depends on: python3, SimpleMFRC522, RPi
# By David Penkowoj, 2021/06/08

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

def main():
  reader = SimpleMFRC522()

  try:
    data = input("New data:")
    print("Scan tag to write")
    reader.write(data)
    print("Done")
  finally:
    GPIO.cleanup()

if __name__ == '__main__':
  main()
