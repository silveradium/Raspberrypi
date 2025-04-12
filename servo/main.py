import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for PWM (GPIO 18 is commonly used)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM with a frequency of 50Hz (typical for servo motors)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)  # Start PWM with 0% duty cycle (servo is at its initial position)

def move_servo(angle):
    # Convert angle to duty cycle (servo expects values between 2% and 12%)
    duty = float(angle) / 18 + 2
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Wait for the servo to reach the position

try:
    while True:
        # Test servo by moving it to different angles
        for angle in range(0, 180, 30):  # Sweep from 0 to 180 degrees
            move_servo(angle)
        for angle in range(180, 0, -30):  # Sweep back from 180 to 0 degrees
            move_servo(angle)

except KeyboardInterrupt:
    print("Program interrupted by user")

finally:
    pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO settings
