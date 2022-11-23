import RPi.GPIO as GPIO
import time

# source: https://keithweaverca.medium.com/controlling-stepper-motors-using-python-with-a-raspberry-pi-b3fbd482f886
# BCM pinout: https://toptechboy.com/understanding-raspberry-pi-4-gpio-pinouts/


# GPIO.setmode(GPIO.BOARD) # NO, this is wrong
GPIO.setmode(GPIO.BCM)

control_pins = [6, 13, 19, 26]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
        ]

for i in range(512):
    for halfstep in range(len(halfstep_seq)):
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)

GPIO.cleanup()
