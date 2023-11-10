import math

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

x = 0
y = 0
radius = 50
angle = 0


@socketio.on("connect")
def handle_connect():
    global x, y, angle
    while True:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        angle += 0.1
        socketio.emit("update_position", {"x": x, "y": y})
        print(f"Sent update: x={x}, y={y}")
        socketio.sleep(1)  # Adjust the delay as needed


if __name__ == "__main__":
    socketio.run(app, debug=True)
