from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(message):
    send(message, broadcast=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True, host="0.0.0.0")

#just test comment for merging 
#haha

