#This code was done with pybricks. Check out how to install pybricks on your hub: https://pybricks.com/learn/getting-started/install-pybricks/

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Direction, Port
 
class TankDrive:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
 
    def drive(self, left_power, right_power):
        if left_power != 0 or right_power != 0:
            self.left_motor.dc(left_power)
            self.right_motor.dc(right_power)
        else:
            self.left_motor.dc(0)
            self.right_motor.dc(0)
 
class Arm:
    def __init__(self, left_arm_motor, right_arm_motor):
        self.left_arm_motor = left_arm_motor
        self.right_arm_motor = right_arm_motor
 
    def punch(self, arm_motor):
        arm_motor.run_time(100, 500, wait=False)
        wait(500)
        arm_motor.run_target(100, 0, wait=False)

    def defense(self):
        self.left_arm_motor.run_target(100, 90, wait=False)
        self.right_arm_motor.run_target(100, 90, wait=False)
        wait(500)
        self.left_arm_motor.run_target(100, 0, wait=False)
        self.right_arm_motor.run_target(100, 0, wait=False)
 
hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
left_arm_motor = Motor(Port.C, Direction.CLOCKWISE)
right_arm_motor = Motor(Port.D, Direction.CLOCKWISE)
 
tank_drive = TankDrive(left_motor, right_motor)
arm = Arm(left_arm_motor, right_arm_motor)
 
print("Waiting for Xbox controller to connect...")
while True:
    try:
        xbox = XboxController()
        print("Xbox controller connected!")
        break
    except Exception as e:
        print(f"Controller not connected: {e}")
        wait(1000)
 
while True:
    triggers = xbox.triggers()
    rt = triggers[1]
    lt = triggers[0]
 
    left_power = 0
    right_power = 0
 
    if rt > 0:
        left_power = rt * 100
        right_power = rt * 100
    elif lt > 0:
        left_power = -lt * 100
        right_power = -lt * 100
 
    joystick = xbox.joystick_left()
    steering_adjustment = joystick[0] * 50
 
    left_power -= steering_adjustment
    right_power += steering_adjustment
 
    tank_drive.drive(left_power, right_power)
 
    if Button.RB in xbox.buttons.pressed():
        arm.punch(right_arm_motor)
    if Button.LB in xbox.buttons.pressed():
        arm.punch(left_arm_motor)
 
    if Button.A in xbox.buttons.pressed():
        arm.defense()
 
    wait(50)

