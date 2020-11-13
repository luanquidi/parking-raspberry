import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.output(10, GPIO.HIGH)
GPIO.output(12, GPIO.HIGH)
time.sleep(1)
GPIO.cleanup()
