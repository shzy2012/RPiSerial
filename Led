import RPi.GPIO as gpio
import time


led_port_list = [14,15,18,23,24,25,8,7]

def led_init():
    gpio.setmode(gpio.BCM)
    for port in led_port_list:
        gpio.setup(port,gpio.OUT,initial=gpio.LOW)


def led_start():
    while True:
        for port in led_port_list:
            gpio.output(port,True)
            time.sleep(0.1) #sleep
            gpio.output(port,False)
            
if __name__== '__main__':
    led_init()
    led_start()

