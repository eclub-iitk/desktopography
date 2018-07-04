# python (flask) side:

import time
from flask import Flask, Response
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue
from flask import render_template
import json
import random

app = Flask(__name__)

def get_finger_state():
    time.sleep(0.1)
    x = random.randint(200,400)
    y =random.randint(200,400)
    clicked = True
    data = { "x" : x, "y" : y, "click" : clicked}
    return data
@app.route("/")
def index():
    return render_template('client.html')
@app.route('/event_stream')
def stream():
    def event_stream():
        while True:
            data = get_finger_state()
            yield 'data: %s\n\n' % json.dumps(data) 
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.debug = True
    server = WSGIServer(("", 5000), app)
    server.serve_forever()
