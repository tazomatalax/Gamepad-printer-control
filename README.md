## Gamepad Printer Control
This Python project allows you to control your OctoPrint-enabled 3D printer using a joystick or gamepad. The code is modular, using the **pygame** library to read input from the joystick and sending commands to the OctoPrint server using the **requests** library.

[Demo video](https://www.youtube.com/shorts/IK1qhjoYjms)

## Requirements
- Python 3
- requests library
- pygame library

You can install the required libraries using pip:

```bash
pip install requests pygame
```

## Configuration
Before running the app, set the following environment variables (recommended: create a .env file):

- `OCTOPRINT_IP`: The IP address of your OctoPrint server.
- `OCTOPRINT_PORT`: The port number of your OctoPrint server.
- `OCTOPRINT_API_KEY`: The API key of your OctoPrint server.

You can find these details in the settings of your OctoPrint server. See `.env.example` for a template.

## Usage
To run the app, use:

```bash
python -m src.main
```

The app will start a loop that reads input from the joystick and sends commands to the OctoPrint server. The X and Y axes of the joystick are mapped to the X and Y axes of the printer, and the buttons are mapped to various commands.

## Button Mappings

You can modify the `button_map` dictionary in `src/main.py` to change the button mappings or add more buttons.
Check the bottom of this page:
https://www.pygame.org/docs/ref/joystick.html
for controller button mappings.

## Throttling
The app includes a delay of 0.2 seconds at the end of each loop iteration to throttle the input from the joystick. You can adjust this delay in `src/main.py` to suit your needs.

## Project Structure

```
src/
    controller.py         # Handles gamepad/joystick input
    octoprint_client.py   # Handles OctoPrint API communication
    main.py               # Entry point
```

## Testing
Unit tests are in the `tests/` directory and can be run with pytest.
