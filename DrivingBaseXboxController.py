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
        # Set motor powers to control the robot's movement
        self.left_motor.dc(left_power)
        self.right_motor.dc(right_power)

class Arm:
    def __init__(self, arm_motor):
        self.arm_motor = arm_motor

    def move_arm(self, down):
        # Move the arm up or down based on the 'down' parameter
        if down:
            self.arm_motor.run_target(10, -90, wait=False)  # Move arm down
        else:
            self.arm_motor.run_target(10, 0, wait=False)  # Move arm up

hub = PrimeHub()
left_motor = Motor(Port.C, Direction.CLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
arm_motor = Motor(Port.E, Direction.CLOCKWISE)

tank_drive = TankDrive(left_motor, right_motor)
arm = Arm(arm_motor)

print("Waiting for Xbox controller to connect...")
while True:
    try:
        xbox = XboxController()
        print("Xbox controller connected!")
        break
    except Exception as e:
        print(f"Controller not connected: {e}")
        wait(1000)

# Define the deadzone threshold
DEADZONE_THRESHOLD = 80  # Adjust this value as needed

while True:
    # Read the triggers for forward and backward movement
    triggers = xbox.triggers()
    rt = triggers[0]
    lt = triggers[1]

    # Calculate the left and right motor powers based on the triggers
    left_power = rt - lt  # RT accelerates forward; LT accelerates backward
    right_power = rt - lt

    # Read the left joystick for steering
    joystick = xbox.joystick_left()
    horizontal = joystick[0]  # Left joystick horizontal axis
    vertical = joystick[1]    # Left joystick vertical axis

    # Apply deadzone to the joystick inputs
    if abs(horizontal) < DEADZONE_THRESHOLD:
        horizontal = 0
    if abs(vertical) < DEADZONE_THRESHOLD:
        vertical = 0

    # Adjust steering based on joystick movement
    # Apply non-linear scaling to make turning slower and more responsive
    steering_adjustment = horizontal * 5 # Reduce this value to make turns slower

    # Apply steering adjustments
    left_power -= steering_adjustment
    right_power += steering_adjustment

    # Drive the robot
    tank_drive.drive(left_power, right_power)

    # Control arm movement with button A
    if Button.A in xbox.buttons.pressed():
        arm.move_arm(down=True)  # Move arm down when button A is pressed
    else:
        arm.move_arm(down=False)  # Move arm up when button A is released

    wait(50)
