#!/usr/bin/env python3

# A script to toggle on a LED for half a second.
# Depends on: python3
# By David Penkowoj, 2021/12/10

import RPi.GPIO as GPIO
import time

def light():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(18, GPIO.OUT)

  GPIO.output(18, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(18, GPIO.LOW)

  GPIO.cleanup()

if __name__ == "__main__":
  light()
