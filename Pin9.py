#import
import RPi.GPIO  as gpio
import time
import sys

# golbal  define

led_port_list = [7,8,9,11,25]

# define def  -----Begin

def led_init():
    gpio.setmode(gpio.BCM)
    for port in led_port_list:
        gpio.setup(port,gpio.OUT,initial=gpio.LOW)
    
def led_start():
    while True:
        if raw_input("Please enter \r\n")=='exit':
            close()
            sys.exit(0)
        for port in led_port_list:
            gpio.output(port,False)
            time.sleep(0.2)
            gpio.output(port,True)
def close():
    gpio.cleanup()
    print 'eixt ...........'
#define  def  -----End


#Main

if __name__ == '__main__':
    print 'init ....'
    led_init()
    print 'start .....'
    led_start()




