from gpiozero import DistanceSensor
import RPi.GPIO as GPIO

# Set up ultrasonic distance sensor
ultrasonic = DistanceSensor(
    echo=16,
    trigger=21,
    max_distance=1
)

# Set up passive buzzer
GPIO.setup(15, GPIO.OUT)
Buzzer = GPIO.PWM(15, 440)
Buzzer.start(50)

def theremin():
    from math import exp
    
    while True:
        freq = (300 * exp(ultrasonic.distance)) + 261
        print(freq)
        Buzzer.ChangeFrequency(freq)

def destroy():
    Buzzer.stop()

if __name__ == '__main__':
    try:
        theremin()
    except KeyboardInterrupt:
        destroy()
