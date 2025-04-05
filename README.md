# Pybricks Boxing, Remote-Controlled Car, and Tank Drive Projects

This repository contains three Python scripts written for LEGO® SPIKE™ Prime robots programmed with [Pybricks](https://pybricks.com/). These projects demonstrate how to control LEGO robots with an Xbox Controller, enabling a boxing robot, a remote-controlled car, or a tank-drive robot with an arm.

---

## Prerequisites

Before running the code, ensure you have the following:

- A LEGO SPIKE™ Prime or equivalent hub.
- Motors connected to your hub as described in the code.
- Pybricks firmware installed on your hub. Follow the [official installation guide](https://pybricks.com/learn/getting-started/install-pybricks/).
- An Xbox Controller (compatible with Bluetooth).

---

## Files in This Repository

### 1. Boxing.py

This script implements a boxing robot that mimics boxing actions using an Xbox controller. The robot includes tank drive movement and arm mechanisms for punching and defending.

#### Features:
- **Tank Drive:** The robot moves forward, backward, and turns using the controller's triggers and left joystick.
- **Punching Mechanism:** Pressing the RB or LB buttons on the controller makes the left or right arm punch.
- **Defense Mode:** Pressing the A button activates both arms to move into a defensive position.

#### Motors Configuration:
- **Left Drive Motor:** Port A
- **Right Drive Motor:** Port B
- **Left Arm Motor:** Port C
- **Right Arm Motor:** Port D

#### Controls:
- **RT/LT (Triggers):** Control forward and backward movement.
- **Left Joystick (X-axis):** Adjust steering.
- **RB Button:** Punch with the right arm.
- **LB Button:** Punch with the left arm.
- **A Button:** Activate defense mode.

![Boxing Robot Demo](https://placeholder.com/boxing_robot.gif)

---

### 2. Remote-Car.py

This script implements a remote-controlled car with steering and an optional arm mechanism. It supports two modes: Car Mode (default) and Arm Mode.

#### Features:
- **Car Mode:**
  - **Steering:** Controlled by the left joystick (X-axis).
  - **Driving Power:** Controlled by RT (accelerate) and LT (reverse).
- **Arm Mode:**
  - The arm motor is controlled by the left joystick (Y-axis).

#### Motors Configuration:
- **Steering Motor:** Port B
- **Power Motor:** Port D
- **Arm Motor (optional):** Port E

#### Controls:
- **Left Joystick (X-axis):** Steering in Car Mode.
- **RT/LT (Triggers):** Drive forward and reverse in Car Mode.
- **Left Joystick (Y-axis):** Control arm movement in Arm Mode.
- **Y Button:** Toggle between Car Mode and Arm Mode.

![Remote-Controlled Car Demo](https://placeholder.com/remote_car.gif)

---

### 3. TankDrive_Arm.py

This script controls a robot using tank drive steering and includes a simple arm mechanism, all controlled via an Xbox controller.

#### Features:
- **Tank Drive:** Uses Xbox triggers (RT/LT) for forward/backward motion and the left joystick (X-axis) for steering.
- **Arm Control:** Button A controls the movement of a single arm motor (down when pressed, up when released).
- **Control Refinements:** Implements joystick deadzone and speed scaling for smoother control.

#### Motors Configuration:
- **Left Drive Motor:** Port C (Clockwise)
- **Right Drive Motor:** Port D (Counter-Clockwise)
- **Arm Motor:** Port E (Clockwise)

#### Controls:
- **RT/LT (Triggers):** Control forward and backward speed (RT forward, LT backward).
- **Left Joystick (X-axis):** Adjust steering.
- **A Button:** Press to move the arm down, release to move it up.

![Tank Drive Arm Demo](https://placeholder.com/tank_arm_robot.gif)

---

## Installation and Usage

1.  Install Pybricks firmware on your hub by following the [official guide](https://pybricks.com/learn/getting-started/install-pybricks/).
2.  Connect the appropriate motors to the hub ports as described in the scripts (`Boxing.py`, `Remote-Car.py`, or `TankDrive_Arm.py`).
3.  Copy the desired script to the hub using the Pybricks code editor. Ensure the script file name matches (e.g., save the provided code as `TankDrive_Arm.py`).
4.  Pair your Xbox controller with the hub via Bluetooth.
5.  Run the script on your hub and control your robot using the Xbox controller.

---

## Troubleshooting

- Ensure the Xbox controller is properly connected to the hub. If it fails to connect, the program will print messages and retry until the connection is established.
- Verify motor connections and directions match the ports and configuration in the specific code file you are using.
- Adjust `DEADZONE_THRESHOLD` and `SPEED_SCALE_FACTOR` in `TankDrive_Arm.py` if controls feel too sensitive or too slow.

---

## Future Improvements

- Add more feedback to the controller, such as vibrations or LED signals.
- Implement additional modes and functionality, such as autonomous features or sensor integration.
- Refine control sensitivity and scaling factors based on specific robot builds.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy building and programming your LEGO robots!
