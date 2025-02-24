import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
u = 3.2895

def dec_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def low(U):
    
    while U>0:
        for num in range(256):
            time.sleep(0.001)
            GPIO.output(dac, dec_bin(num))
            U -= 0.0129
    return U

def high(U):
    
    while U < 3.2895:
        for num in range(255, -1, -1):
            time.sleep(0.001)
            GPIO.output(dac, dec_bin(num))
            U += 0.0129
    
    return U

try:
    while True:
        u = low(u)
        u = high(u)

except KeyboardInterrupt:
            print('The program was stopped by keyboard')
     
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


