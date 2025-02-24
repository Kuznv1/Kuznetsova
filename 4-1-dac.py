import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        num = round(float(input()))
        GPIO.output(dac, dec_bin(num))
        one = round((3.3/256), 4)

        Vol = [one*i for i in range(256)]
        U = Vol[num]
        print(U)
        
except KeyboardInterrupt:
            print('The program was stopped by keyboard')
     




finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()