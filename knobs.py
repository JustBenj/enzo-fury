# Get the knobs

import RPi.GPIO as GPIO
import time


left_knob_a = 26 # white
left_knob_b = 21 # black

right_knob_a = 19 # orange
right_knob_b = 20 # green

GPIO.setmode(GPIO.BCM)

GPIO.setup(left_knob_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(left_knob_b, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(right_knob_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(right_knob_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

old_left_state = 0
left_state = 0

old_right_state = 0
right_state = 0

CCW = 0
CW = 1

left_direction = CCW
right_direction = CCW

while True:
    time.sleep(0.1)
    
    lka = GPIO.input(left_knob_a)
    lkb = GPIO.input(left_knob_b)
    rka = GPIO.input(right_knob_a)
    rkb = GPIO.input(right_knob_b)
    old_left_state = left_state
    left_state = (lka<<1)+lkb

    old_right_state = right_state
    right_state = (rka<<1)+rkb

    #print("lka: %d lkb: %d rka: %d rkb %d" % (lka, lkb, rka, rkb))
    #print("left: %d right %d" % (left_state, right_state))
    if old_left_state != left_state:
        
        if old_left_state == 0:
            if left_state == 1:
                left_direction = CW
            if left_state == 2 or left_state == 3:
                left_direction = CCW

        if old_left_state == 1:
            if left_state == 0:
                left_direction = CCW
            if left_state == 2 or left_state == 3:
                left_direction = CW

        if old_left_state == 2:
            if left_state == 1:
                left_direction = CCW
            if left_state == 0:
                left_direction = CW

        if old_left_state == 3:
            if left_state == 1:
                left_direction = CCW
            if left_state == 0:
                left_direction = CW

        print("Left: %d" % left_direction)
        print("\n")

    if old_right_state != right_state:
        
        if old_right_state == 0:
            if right_state == 1:
                right_direction = CW
            if right_state == 2 or right_state == 3:
                right_direction = CCW

        if old_right_state == 1:
            if right_state == 0:
                right_direction = CCW
            if right_state == 2 or right_state == 3:
                right_direction = CW

        if old_right_state == 2:
            if right_state == 1:
                right_direction = CCW
            if right_state == 0:
                right_direction = CW

        if old_right_state == 3:
            if right_state == 1:
                right_direction = CCW
            if right_state == 0:
                right_direction = CW

        print("Right: %d" % right_direction)
        print("\n")

    



