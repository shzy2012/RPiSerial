import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

gpio.setup(11,gpio.IN)
gpio.setup(12,gpio.OUT)

input_value = gpio.input(11)

gpio.output(12,gpio.HIGH)

gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.IN)
gpio.setup(18,gpio.OUT)
input_value = gpio.input(17)
gpio.output(18,gpio.HIGH)
