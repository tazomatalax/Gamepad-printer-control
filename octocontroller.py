try:
    import requests
    import pygame
    import time
except ImportError:
    print("Please install the 'requests' and 'pygame' libraries.")
    # You can use pip to install the libraries:
    # !pip install requests
    # !pip install pygame
    # or
    # !pip3 install requests
    # !pip3 install pygame

# Define the IP address of your OctoPrint server
octoprint_ip = "your_ip_here"

# Define the port number of your OctoPrint server
octoprint_port = "80"

# Define the API key of your OctoPrint server
api_key = "your_api_key_here"

# Define the button mappings
button_map = {
    0: {"command": "jog", "x": 10},  # Move X by 10 to the right
    1: {"command": "jog", "x": -10},  # Move X by 10 to the left
    2: {"command": "jog", "y": 10},  # Move Y by 10 to the front
    3: {"command": "jog", "y": -10},  # Move Y by 10 to the back
    4: {"command": "home", "axes": ["x", "y"]},  # Home X and Y axes
    5: {"command": "home", "axes": ["z"]},  # Home Z axis
    # Add more buttons as needed
}



# URL for printhead control
url = "http://{0}:{1}/api/printer/printhead".format(octoprint_ip, octoprint_port)
# Initialize the pygame library
pygame.init()

# Initialize the video system
pygame.display.init()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Initialize the gamepad
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

# Define a threshold for the joystick's X and Y values
threshold = 0.5

# Main game loop
while True:
    # Process events
    pygame.event.pump()

    # Get the X and Y positions of the thumbstick (axes 0 and 1)
    x = joystick.get_axis(0)
    y = joystick.get_axis(1)

    # Create a command based on the thumbstick position
    if x > threshold:
        command = {"command": "jog", "x": 10}  # Move X by 10 to the right
    elif x < -threshold:
        command = {"command": "jog", "x": -10}  # Move X by 10 to the left
    elif y > threshold:
        command = {"command": "jog", "y": 10}  # Move Y by 10 to the front
    elif y < -threshold:
        command = {"command": "jog", "y": -10}  # Move Y by 10 to the back
    else:
        continue  # Skip this iteration if the thumbstick is centered

    # Send a POST request to the OctoPrint server
    response = requests.post(url, json=command, headers={'X-Api-Key': api_key})

    # Check the response
    if response.status_code == 204:
        print('Request was successful.')
    else:
        print('Request failed. Status code:', response.status_code)

    # Add a delay to throttle the input
    time.sleep(0.2)
  

    # for event in pygame.event.get():
    #     # Check for a button press event
    #     if event.type == pygame.JOYBUTTONDOWN:
    #         # Get the command from the button map
    #         command = button_map.get(event.button)
    #         if command:
    #             # Send a POST request to the OctoPrint server
    #             response = requests.post(url, json=command, headers={'X-Api-Key': api_key})

    #             # Check the response
    #             if response.status_code == 204:
    #                 print('Request was successful.')
    #             else:
    #                 print('Request failed. Status code:', response.status_code)





