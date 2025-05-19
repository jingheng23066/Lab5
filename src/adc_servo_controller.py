import RPi.GPIO as GPIO
from time import sleep

# Define PWM globally so we can reuse it
PWM = None

def init():
    global PWM
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)
    PWM = GPIO.PWM(26, 50)  # 50Hz PWM frequency
    PWM.start(0)  # Start with 0% duty cycle

# Set servo angle between 0 and 180 degrees
def set_servo_position(position):
    global PWM
    # Convert angle to duty cycle: range typically 2 to 12
    duty_cycle = (-10 * position) / 180 + 12
    print("Servo angle:", position, "-> PWM duty cycle:", duty_cycle)
    PWM.ChangeDutyCycle(duty_cycle)
    sleep(0.05)

def cleanup():
    global PWM
    PWM.stop()
    GPIO.cleanup()
