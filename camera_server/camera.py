from flask import Flask, Response
from picamera2 import Picamera2
# type: ignore
import cv2

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"format": "XRGB8888", "size": (640, 480)}))
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        
        # Flip the frame vertically (upside down)
        frame = cv2.flip(frame, 0)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return '<h1>Raspberry Pi Camera</h1><img src="/video">'

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
