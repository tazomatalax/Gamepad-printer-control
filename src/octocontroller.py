import requests
import pygame
import time
import os

# Configuration: allow environment variable overrides
OCTOPRINT_IP = os.getenv('OCTOPRINT_IP', "your_ip_here")
OCTOPRINT_PORT = os.getenv('OCTOPRINT_PORT', "80")
API_KEY = os.getenv('OCTOPRINT_API_KEY', "your_api_key_here")

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



# URL for printhead control
url = f"http://{OCTOPRINT_IP}:{OCTOPRINT_PORT}/api/printer/printhead"

pygame.init()
pygame.display.init()

# Try to initialize the first joystick/gamepad
if pygame.joystick.get_count() == 0:
    print("No joystick/gamepad detected. Please connect one and restart.")
    exit(1)

joystick = pygame.joystick.Joystick(0)
joystick.init()

threshold = 0.5  # Thumbstick deadzone threshold

def send_octoprint_command(command):
    try:
        response = requests.post(url, json=command, headers={'X-Api-Key': API_KEY})
        if response.status_code == 204:
            print('Request was successful:', command)
        else:
            print('Request failed. Status code:', response.status_code, command)
    except Exception as e:
        print('Error sending request:', e)

print("Ready. Use the gamepad to control the printer.")

while True:
    pygame.event.pump()
    x = joystick.get_axis(0)
    y = joystick.get_axis(1)
    command = None
    # Thumbstick movement
    if x > threshold:
        command = {"command": "jog", "x": 10}
    elif x < -threshold:
        command = {"command": "jog", "x": -10}
    elif y > threshold:
        command = {"command": "jog", "y": 10}
    elif y < -threshold:
        command = {"command": "jog", "y": -10}
    if command:
        send_octoprint_command(command)
        time.sleep(0.2)
        continue
    # Button presses
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            command = button_map.get(event.button)
            if command:
                send_octoprint_command(command)
    time.sleep(0.05)





