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

def bin1(A):
    num = 0
    st = 7
    
    for i in A:
        num += i*2**st
        st-=1
        
    
    return num


def adc(a):
    D = [0 for i in range(8)]
    one = round((3.3/256), 4)
    Vol = [one*i for i in range(256)]
    
    
    for i in range(8):
        D[i] = 1
        
        number = (D)
        GPIO.output(dac, number) 
        time.sleep(0.1)
        #print(bin1(D),GPIO.input(comp) )
        if GPIO.input(comp) == 1:
            D[i] = 0

    
    GPIO.output(dac, D)     
    return Vol[bin1(D)]


try:
    while True:
        
        print(adc(1))
        time.sleep(0.1)
        
except KeyboardInterrupt:
            print('The program was stopped by keyboard')


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()