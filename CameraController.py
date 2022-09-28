from typing import Any

import cv2 as cv
import paho.mqtt.client as mqtt
import base64
import threading

local_broker_address = "127.0.0.1"
local_broker_port = 1883
sendingVideoStream = False


def send_video_stream(message) -> Any:
    global sendingVideoStream
    cap = cv.VideoCapture(0)
    splitted = message.split('/')
    origin = splitted[0]
    while sendingVideoStream:
        # Read Frame
        _, frame = cap.read()
        # Encoding the Frame
        _, buffer = cv.imencode('.jpg', frame)
        # Converting into encoded bytes
        jpg_as_text = base64.b64encode(buffer)
        # Publishing the Frame on the Topic home/server
        client.publish('cameraService/'+origin+'/videoFrame', jpg_as_text)
    cap.release()


def on_message(client, userdata, message) -> Any:
    global sendingVideoStream
    splitted = message.topic.split('/')
    origin = splitted[0]
    destination = splitted[1]
    command = splitted[2]

    if command == 'connectPlatform':
        print('Camera service connected by ' + origin)

        # aqui en realidad solo debería subscribirse a los comandos que llegan desde el dispositivo
        # que ordenó la conexión, pero esa información no la tiene porque el origen de este mensaje
        # es el gate. NO COSTARIA MUCHO RESOLVER ESTO. HAY QUE VER SI ES NECESARIO

        client.subscribe('+/cameraService/#')

    if command == 'takePicture':
        print('Take picture')
        cap = cv.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
        for n in range(10):
            # this loop is required to discard first frames
            ret, frame = cap.read()
            _, buffer = cv.imencode('.jpg', frame)
            # Converting into encoded bytes
            jpg_as_text = base64.b64encode(buffer)
            client.publish('cameraService/' + origin + '/picture', jpg_as_text)

    if command == 'startVideoStream':
        sendingVideoStream = True
        w = threading.Thread(target=send_video_stream, args=(message.topic,))
        w.start()

    if command == 'stopVideoStream':
        sendingVideoStream = False


client = mqtt.Client("Camera service")
client.on_message = on_message
client.connect(local_broker_address, local_broker_port)
client.loop_start()
print('Waiting connection from DASH...')
client.subscribe('gate/cameraService/connectPlatform')
