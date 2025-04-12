from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Left Motor pin
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
# Left Motor pin
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Servo setup on GPIO 27
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18, 50)  # 50Hz
servo.start(7.5)  # Initialize at 90°

# Motor control functions
def forward():
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)

def backward():
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

def stop():
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

# Flask setup
app = Flask(__name__)

def set_servo_angle(angle):
    duty = (0.05 * 50) + (0.19 * 50) * (angle / 180.0)
    servo.ChangeDutyCycle(duty)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    key = request.form['key']
    state = request.form['state']

    if key == 'ArrowUp':
        if state == 'down':
            forward()
        elif state == 'up':
            stop()

    elif key == 'ArrowDown':
        if state == 'down':
            backward()
        elif state == 'up':
            stop()

    elif key == 'ArrowLeft':
        if state == 'down':
            set_servo_angle(120)  # Turn servo to 0°
        elif state == 'up':
            set_servo_angle(90)  # Return to center

    elif key == 'ArrowRight':
        if state == 'down':
            set_servo_angle(60)  # Turn servo to 180°
        elif state == 'up':
            set_servo_angle(90)  # Return to center

    return ('', 204)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        servo.stop()
        GPIO.cleanup()
