from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time


# GPIO setup
GPIO.setmode(GPIO.BCM)

# Left Motor pins
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
# Right Motor pins
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)



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

def left():
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)

def right():
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

stop()

# Flask setup
app = Flask(__name__)

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
            left()
        elif state == 'up':
            stop()

    elif key == 'ArrowRight':
        if state == 'down':
            right()
        elif state == 'up':
            stop()

    return ('', 204)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
