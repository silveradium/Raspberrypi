import RPi.GPIO as GPIO
import time

LED_PIN = 17  # GPIO number

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Blink loop
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)   # LED OFF
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by user")

# Cleanup
GPIO.cleanup()
