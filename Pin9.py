#import
import RPi.GPIO  as gio
import time

# golbal  define

led_port_list = [9,11]

# define def  -----Begin

def led_ini():
    gpio.setmode(gpio.BCM)
    for port led_port_list:
        gpio.setup(port,gpio.OUT,initial=gpio.LOW)
    
def led_start():
    while True:
        for port led_port_list:
            gpio.output(port,True)
            time.sleep(0.1)
            gpio.output(port,False)

#define  def  -----End


#Main

if __name__ == '__main__':
    led_init()
    led_start()




