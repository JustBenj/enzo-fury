# Get the knobs

import RPi.GPIO as GPIO
import time


left_knob_a = 26 # white
left_knob_b = 21 # black

right_knob_a =  # orange
right_knob_b =  # green

GPIO.setmode(GPIO.BCM)

GPIO.setup(left_knob_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(left_knob_b, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(right_knob_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(right_knob_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

old_left_state = 0
left_state = 0

old_right_state = 0
right_state = 0

while True:
    time.sleep(0.02)
    
    lka = GPIO.input(left_knob_a)
    lkb = GPIO.input(left_knob_b)
    rka = GPIO.input(right_knob_a)
    rkb = GPIO.input(right_knob_b)

    old_left_state = left_state
    left_state = lka + lkb

    old_right_state = right_state
    right_state = rka + rkb


    if old_left_state != left_state or old_right_state != right_state:
        print("Left: %d", lka + lkb)
        print("Right: %d", rka + rkb)




