# python (flask) side:

import time
from flask import Flask, Response   
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue
from flask import render_template
import json
import random
import socket
UDP_IP = "192.168.0.122"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
app = Flask(__name__)

def get_finger_state():
    #time.sleep(0.1)
    x = random.randint(200,400)
    y =random.randint(200,400)
    data2, addr = sock.recvfrom(1024) # buffer size is 1024 bytes    
    data2 = data2.decode()
    split_data = data2.split(',')
    x = int(split_data[0])
    y = int(split_data[1])
    is_clicked = int(split_data[2])
    print("data",x,y,is_clicked)
    print("data",data2)    
    clicked = 1
    data = { "x" : x, "y" : y, "click" : is_clicked}
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
