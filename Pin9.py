#import
import RPi.GPIO  as gio
import time
import sys

# golbal  define

led_port_list = [9,11]

# define def  -----Begin

def led_ini():
    gpio.setmode(gpio.BCM)
    for port led_port_list:
        gpio.setup(port,gpio.OUT,initial=gpio.LOW)
    
def led_start():
    while True:
        print 'exit...'
        if raw_input("Please enter \r\n")=='exit':
            sys.exit(0)
        for port led_port_list:
            gpio.output(port,True)
            time.sleep(0.1)
            gpio.output(port,False)

#define  def  -----End


#Main

if __name__ == '__main__':
    print 'init ....'
    led_init()
    print 'start .....'
    led_start()




