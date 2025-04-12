from flask import Flask, render_template, request, Response
import RPi.GPIO as GPIO
import time
from picamera2 import Picamera2
# type: ignore
import cv2

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

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"format": "XRGB8888", "size": (640, 480)}))
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        
        # Flip the frame vertically (upside down)
        frame = cv2.flip(frame, 1)
        frame = cv2.flip(frame, 0)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Flask setup
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


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
