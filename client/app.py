import socketio
import json
# standard Python
server_url = "http://localhost:3000/"
sio = socketio.Client()
sio.connect(server_url)


@sio.event
def connect():
    print("I'm connected!")


@sio.on('rangeChanged')
def rangeChanged(data):
    mamad = json.loads(data)
    print(type(mamad))
    for key in mamad:
        print (key,mamad[key])

