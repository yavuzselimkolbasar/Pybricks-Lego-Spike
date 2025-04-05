# Pybricks Boxing, Remote-Controlled Car, and Driving Base Projects

This repository contains three Python scripts written for LEGO® SPIKE™ Prime robots programmed with [Pybricks](https://pybricks.com/). These projects demonstrate how to control different LEGO robot builds with an Xbox Controller, including a boxing robot, a remote-controlled car, and the standard Driving Base.

*(Updated Apr 5, 2025 to include user-provided YouTube link)*

---

## Prerequisites

Before running the code, ensure you have the following:

- A LEGO SPIKE™ Prime or equivalent hub.
- Motors connected to your hub as described in the code for the specific project you are building.
- Pybricks firmware installed on your hub. Follow the [official installation guide](https://pybricks.com/learn/getting-started/install-pybricks/).
- An Xbox Controller (compatible with Bluetooth).
- **For `DrivingBaseXboxController.py`:** You should have built the standard [**Driving Base model**](https://spike.legoeducation.com/prime/models/bltc58e302d70cf6530). If you intend to use the arm control feature, you also need the [**Driving Base Arm attachment**](https://spike.legoeducation.com/prime/models/blte7efff9c7c96c9cb).
- **For `Remote-Car.py`:** You should have built a robot with car-style steering (using one motor for steering wheels and another for driving power, potentially with gears).

---

## Files in This Repository

*(Based on file list from Apr 5, 2025)*

### 1. Boxing.py
*(Last updated: Jan 24, 2025)*

This script implements a boxing robot that mimics boxing actions using an Xbox controller. The robot includes **tank drive** movement (controlling left and right wheels independently for speed and turning) and arm mechanisms for punching and defending.

#### Features:
- **Tank Drive:** The robot moves forward, backward, and turns using the controller's triggers and left joystick, controlling power to left/right motors.
- **Punching Mechanism:** Pressing the RB or LB buttons on the controller makes the left or right arm punch.
- **Defense Mode:** Pressing the A button activates both arms to move into a defensive position.

#### Motors Configuration:
- **Left Drive Motor:** Port A
- **Right Drive Motor:** Port B
- **Left Arm Motor:** Port C
- **Right Arm Motor:** Port D

#### Controls:
- **RT/LT (Triggers):** Control forward and backward movement.
- **Left Joystick (X-axis):** Adjust steering (by varying left/right motor speeds).
- **RB Button:** Punch with the right arm.
- **LB Button:** Punch with the left arm.
- **A Button:** Activate defense mode.

![Boxing Robot Demo](https://placeholder.com/boxing_robot.gif)

---

### 2. Remote-Car.py
*(No recent update specified, assumed stable)*

This script controls a robot built **like a car**, featuring a dedicated steering motor and a separate power motor. This setup uses three motors: one for steering wheel direction, one for driving power (often **upgraded with a gear system** for better torque or speed), and an optional third motor for an arm. It supports toggling between driving/steering (Car Mode) and arm control (Arm Mode) using the Xbox controller.

#### Features:
- **Car-Style Steering:** Uses a dedicated motor (Port B) for precise steering control of front wheels, mimicking a real car (steering mechanism inspired by [this video](https://youtu.be/-hhYf52du5Q?si=4xTRQlIgEBRraBmb)), controlled by the left joystick (X-axis) in Car Mode.
- **Geared Power Drive:** Designed for a main drive motor (Port D) providing forward/reverse power, potentially using gears for enhanced performance, controlled by RT/LT triggers in Car Mode.
- **Optional Arm Control:** Allows control of an arm motor (Port E) using the left joystick (Y-axis) when switched to Arm Mode.
- **Mode Switching:** Use the Y button to toggle between Car Mode (drive/steer) and Arm Mode (arm control).

#### Motors Configuration:
- **Steering Motor:** Port B (Controls wheel direction)
- **Power Motor:** Port D (Drives the robot forward/backward, often geared)
- **Arm Motor (optional):** Port E

#### Controls:
- **Left Joystick (X-axis):** Controls steering angle in Car Mode.
- **RT/LT (Triggers):** Drive forward and reverse in Car Mode.
- **Left Joystick (Y-axis):** Control arm movement in Arm Mode.
- **Y Button:** Toggle between Car Mode and Arm Mode.

![Remote-Controlled Car Demo](https://placeholder.com/remote_car.gif)

---

### 3. DrivingBaseXboxController.py
*(Last updated: Apr 5, 2025)*

This script provides Xbox Controller control for the standard **[LEGO Education SPIKE Prime Driving Base](https://spike.legoeducation.com/prime/models/bltc58e302d70cf6530)**. It uses **tank drive** steering (controlling left and right wheels independently for speed and turning) and includes control for the optional **[Driving Base Arm attachment](https://spike.legoeducation.com/prime/models/blte7efff9c7c96c9cb)** connected to Port E using the 'A' button.

#### Features:
- **Tank Drive:** Specifically configured for the standard Driving Base build. Uses Xbox triggers (RT/LT) for forward/backward motion and the left joystick (X-axis) for steering by varying left/right motor speeds.
- **Arm Control:** Button A controls the movement of the standard Driving Base Arm attachment (Port E) when added (down when pressed, up when released).
- **Control Refinements:** Implements joystick deadzone and speed scaling for smoother control.

#### Motors Configuration (Matches Standard Driving Base + Optional Arm):
- **Left Drive Motor:** Port C (Clockwise)
- **Right Drive Motor:** Port D (Counter-Clockwise)
- **Optional Arm Motor:** Port E (Clockwise) - *Requires [Arm Attachment](https://spike.legoeducation.com/prime/models/blte7efff9c7c96c9cb)*

#### Controls:
- **RT/LT (Triggers):** Control forward and backward speed (RT forward, LT backward).
- **Left Joystick (X-axis):** Adjust steering (by varying left/right motor speeds).
- **A Button:** Press to move the optional arm down, release to move it up.

![Driving Base Demo](https://placeholder.com/driving_base_xbox.gif)

---

## Installation and Usage

1.  Build your desired robot (Boxing Robot, Remote Car, or the standard Driving Base using the links provided above), ensuring the build matches the control style (Tank Drive vs Car Steering). Add the Arm attachment if needed.
2.  Install Pybricks firmware on your hub by following the [official guide](https://pybricks.com/learn/getting-started/install-pybricks/).
3.  Connect the appropriate motors to the hub ports as described in the chosen script (`Boxing.py`, `Remote-Car.py`, or `DrivingBaseXboxController.py`). Pay attention to the motor roles (Drive, Steering, Arm) and required attachments.
4.  Copy the corresponding script to the hub using the Pybricks code editor.
5.  Run the script on your hub
6.  Pair your Xbox controller with the hub via Bluetooth and control your robot using the Xbox controller.

---

## Troubleshooting

- Ensure the Xbox controller is properly connected to the hub. If it fails to connect, the program will print messages and retry until the connection is established.
- Verify motor connections and directions match the ports and configuration in the specific code file you are using. Check the motor roles and directions (Clockwise/Counter-Clockwise) carefully. Ensure the Arm attachment is built correctly if using arm controls.
- Adjust `DEADZONE_THRESHOLD` and `SPEED_SCALE_FACTOR` in `DrivingBaseXboxController.py` if controls feel too sensitive or too slow for your preference. Sensitivity adjustments might also be needed for `Remote-Car.py` or `Boxing.py` depending on the build.

---

## Future Improvements

- Add more feedback to the controller, such as vibrations or LED signals. Such as FFB can make the response time higher.
- Implement additional modes and functionality, such as autonomous features or sensor integration.
- Refine control sensitivity and scaling factors based on specific robot builds. Add options for configuring steering sensitivity in `Remote-Car.py`.

---

## License

This project is licensed under the MIT License. See the LICENSE file (added Jan 30, 2025) for more details.

---

Enjoy building and programming your LEGO robots!
