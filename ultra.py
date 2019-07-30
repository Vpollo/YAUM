#!/usr/bin/env python

import sys
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')
import Jetson.GPIO as GPIO
import time


class Ultra:
    def __init__(self, trig, echo):
        # Pin Definitions
        self.trig_output_pin = trig 
        self.echo_input_pin = echo  

    def setUp():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trig_output_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.echo_input_pin, GPIO.IN)
        
        
    def distance_to_spitball():
        distance = 0
        GPIO.output(self.trig_output_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig_output_pin, GPIO.LOW)

        pulse_start = time.time()
        while GPIO.input(self.echo_input_pin)==0:
            pulse_start = time.time()

            pulse_end = time.time()
            while GPIO.input(self.echo_input_pin)==1:
                pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration * 17150
                distance = round(distance, 2)
        return distance


if __name__ == '__main__':
    distance_to_spitball()
