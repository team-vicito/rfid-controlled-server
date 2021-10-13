#!/usr/bin/env python3

# A simplified system for using RFID technology in combination with a webserver.
# Depends on: python3, SimpleMFRC522, RPi
# By David Penkowoj, 2021/06/08

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

def main():
  reader = SimpleMFRC522()

  try:
    data = input("Please enter the new ID data:\n")
    print("Please scan the ID to write")
    reader.write(data)
    print("Data '" + data + "' successfully written to ID.")
  except:
    print("Failed to write to ID.")
  finally:
    GPIO.cleanup()

if __name__ == '__main__':
  main()
