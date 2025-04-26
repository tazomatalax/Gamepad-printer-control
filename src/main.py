"""
main.py

Entry point for Gamepad Printer Control.
"""
import os
import time
from controller import GamepadController
from octoprint_client import OctoPrintClient

# Button mappings for gamepad buttons
button_map = {
    0: {"command": "jog", "x": 10},   # Move X by 10 to the right
    1: {"command": "jog", "x": -10},  # Move X by 10 to the left
    2: {"command": "jog", "y": 10},   # Move Y by 10 to the front
    3: {"command": "jog", "y": -10},  # Move Y by 10 to the back
    4: {"command": "home", "axes": ["x", "y"]},  # Home X and Y axes
    5: {"command": "home", "axes": ["z"]},        # Home Z axis
    # Add more buttons as needed
}

OCTOPRINT_IP = os.getenv('OCTOPRINT_IP', "your_ip_here")
OCTOPRINT_PORT = os.getenv('OCTOPRINT_PORT', "80")
API_KEY = os.getenv('OCTOPRINT_API_KEY', "your_api_key_here")


def main():
    """
    Main event loop for gamepad printer control.
    """
    controller = GamepadController()
    client = OctoPrintClient(OCTOPRINT_IP, OCTOPRINT_PORT, API_KEY)
    print("Ready. Use the gamepad to control the printer.")
    while True:
        command = controller.get_axis_command()
        if command:
            client.send_command(command)
            time.sleep(0.2)
            continue
        for event in controller.get_button_events():
            button_command = button_map.get(event.button)
            if button_command:
                client.send_command(button_command)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
