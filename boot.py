import time
import board
import neopixel
from gpiozero import Button
from signal import pause
import schedule as s
import requests
import CameraService
import LEDsService
import AutopilotService
import threading
import os


def internet_on():
    try:
       req = requests.get('http://www.upc.edu')
       print ('resultado ', req.status_code)
       if req.status_code != 200:
           return False
       else:
           return True
    except requests.exceptions.RequestException as e:  
       return False





def task ():
    global pixels
    global red, green, blue
    global cont, s
    global communication_mode, end
    cont = cont + 1
    print (cont)
    if cont == 20:
        if green:
            communication_mode = 'local'
        else:
            communication_mode = 'global'
        print ('fin')
        end = True
        return s.CancelJob
    elif green:
        if cont%2 == 0:
            pixels[0] = (0, 0, 0)
        else:
            pixels[0] = (0, 255, 0)
    else:
        if cont % 2 == 0:
            pixels[0] = (0, 0, 0)
        else:
            pixels[0] = (0, 0, 255)


def buttonPressed ():
    global red, green, blue
    global cont, s
    global pixels

    if green:
        green = False
        blue = True
        pixels[0] = (0, 0, 255)
        cont = 0

    else:
        green = True
        blue = False
        pixels[0] = (0, 255, 0)
        cont = 0



def bootSequence (external_broker, username, password):
    global pixels
    global red, green, blue
    global communication_mode, end, cont
   
     
    pixels = neopixel.NeoPixel (board.D18,5)
    pixels[0] = (255, 0, 0)
    if not internet_on():
       pixels[0] = (0,255,0)
       communication_mode = 'local'
    else:
       green = True
       blue = False
       button = Button(2)
       button.when_pressed = buttonPressed
       end = False
       cont =0
       s.every(0.5).seconds.do(task)
       while not end:
         s.run_pending()

    
    print ('Communicacion mode: ', communication_mode)
    if communication_mode == 'global' and external_broker == None:
        print ('ERROR: External broker must be specified in case of global communication mode')
    else:

    	cmd = 'mosquitto -v -c /etc/mosquitto/mosquitto1884.conf -d'
    	os.system(cmd)
    	print ('Internal broker started at port 1884')
    	print ('Starting LEDs service')
    	ls = threading.Thread(target=LEDsService.LEDsService(
        	communication_mode, 
        	'production',
        	external_broker,
        	username,
        	password
    	))

    	ls.start()
   
    	print ('Starting autopilot service')
    	pas = threading.Thread (target = AutopilotService.AutopilotService(
        	communication_mode,
        	'production',
        	external_broker,
        	username,
        	password
    	))

    	pas.start()
   
    	print ('Starting camera service')
    	cs = threading.Thread(target=CameraService.CameraService(
        	communication_mode,
        	'production',
        	external_broker,
        	username,
        	password
    	))
    	cs.start()


if __name__ == '__main__':

    import sys
    username = None
    password = None
    external_broker = None
    if len(sys.argv) > 1:
    	external_broker = sys.argv[1] # in case connection_mode is global
    	if external_broker == 'classpip.upc.edu':
        	username = sys.argv[2]
        	password = sys.argv[3]

    bootSequence(external_broker, username, password)

