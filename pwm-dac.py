import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
# GPIO.setup(9, GPIO.OUT)
p = GPIO.PWM(24, 50)

#p = GPIO.PWM(9, 50)
p.start(0)
try:
    while True:
        k = int(input())
        p.start(k)
        one = 3.3/100
        print(one*k)

finally:
    p.stop
    GPIO.cleanup()