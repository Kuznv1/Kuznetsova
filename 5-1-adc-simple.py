import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
comp = 14
troyka = 13
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]   

def adc():
    number = 1
    while not GPIO.input(comp) and number != 255:
        time.sleep(0.1)
        number += 1        
        GPIO.output(dac, dec_bin(number))
        one = round((3.3/256), 4)

        Vol = [one*i for i in range(256)]
        U = Vol[number]
        return U

try:
    while True:
        print(adc())
        
except KeyboardInterrupt:
            print('The program was stopped by keyboard')
     




finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()