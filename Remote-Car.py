#This code was done in pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Direction, Port
 
class Car:
    def __init__(self, steering_motor, power_motor):
        self.steering_motor = steering_motor
        self.power_motor = power_motor
 
    def steer(self, angle):
        max_steering_angle = 90
        steering_angle = (angle / 100) * max_steering_angle
        self.steering_motor.run_target(speed=600, target_angle=steering_angle, wait=False)
 
    def drive_power(self, power):
        scaled_power = power * 10
        scaled_power = max(-1000, min(1000, scaled_power))  
        self.power_motor.dc(scaled_power)
 
    def check_load_and_feedback(self, controller, threshold=50):
        pass
 
class Arm:
    def __init__(self, vertical_motor):
        self.vertical_motor = vertical_motor
 
    def control(self, joystick_y):
        vertical_speed = 0.4
        self.vertical_motor.dc(joystick_y * vertical_speed)
 
hub = PrimeHub()
 
steering_motor = Motor(Port.B, Direction.CLOCKWISE)
power_motor = Motor(Port.D, Direction.CLOCKWISE)
vertical_motor = Motor(Port.E, Direction.CLOCKWISE)
 
car = Car(steering_motor, power_motor)
arm = Arm(vertical_motor)
 
print("Waiting for Xbox controller to connect...")
while True:
    try:
        xbox = XboxController()
        print("Xbox controller connected!")
        break
    except Exception as e:
        print(f"Controller not connected: {e}")
        wait(1000)  
 
arm_mode = False
 
while True:
    if Button.Y in xbox.buttons.pressed():
        arm_mode = not arm_mode
        mode_name = "Arm Mode" if arm_mode else "Car Mode"
        print(f"Mode toggled. Current mode: {mode_name}")
        wait(300)
    
    if arm_mode:
        joystick = xbox.joystick_left()
        arm.control(joystick[1])  
    else:
        joystick = xbox.joystick_left()
        car.steer(joystick[0])  
        trigger_values = xbox.triggers()
        drive_power = trigger_values[1] - trigger_values[0]  
        car.drive_power(drive_power)
        car.check_load_and_feedback(xbox)
 
    wait(50)
