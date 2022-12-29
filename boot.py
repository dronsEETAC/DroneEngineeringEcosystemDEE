
import time
import board
import neopixel
from gpiozero import Button
from signal import pause
import schedule as s
import requests
import CamSerCirco
import LEDserv
import AutopilotService
import threading
def task ():
    global pixels
    global red, green, blue
    global cont, s
    global model, end
    cont = cont + 1
    print (cont)
    if cont == 20:
        if green:
            model = 'local'
        else:
            model = 'global'
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


def bootSequence ():
    global pixels
    global red, green, blue
    global model, end, cont
    pixels = neopixel.NeoPixel (board.D18,5)
    pixels[0] = (255, 0, 0)
    req = requests.get('http://clients3.google.com/generate_204')
    if req.status_code != 204:
       pixels[0] = (0,255,0)
       print ('model ', 'local')
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


    print ('model ', model)
    #print ('Starting LEDs service')
    #ls = threading.Thread(target=LEDserv.LEDsService(model))
    #ls.start()
    print ('Starting autopilot service')
    pas = threading.Thread (target = AutopilotService.AutoServ(model))
    pas.start()
    #print ('Starting camera service')
    #cs = threading.Thread(target=CamSerCirco.cameraService(model))
    #cs.start()


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    bootSequence()
