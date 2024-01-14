# Copyright(c) 2023 Emmanuel Fofeyin All rights reserved.
# Created by : Emmanuel Fofeyin Vovk
# Created on : Jam 2024
# TEJ3M-Unit2-06.py File.

import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP13, echo_pin=board.GP12)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying")
    time.sleep(0.1)
