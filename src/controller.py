"""
controller.py

Handles gamepad/joystick input using pygame.
"""
import pygame
from typing import Optional, Dict, Any

class GamepadController:
    """
    Handles gamepad/joystick input using pygame.
    """
    def __init__(self, threshold: float = 0.5):
        """
        Initialize the gamepad controller.

        Args:
            threshold (float): Deadzone threshold for thumbstick.
        """
        pygame.init()
        pygame.display.init()
        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No joystick/gamepad detected. Please connect one and restart.")
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.threshold = threshold

    def get_axis_command(self) -> Optional[Dict[str, Any]]:
        """
        Get jog command from thumbstick axes.

        Returns:
            Optional[Dict[str, Any]]: Jog command if movement detected, else None.
        """
        pygame.event.pump()
        x = self.joystick.get_axis(0)
        y = self.joystick.get_axis(1)
        if x > self.threshold:
            return {"command": "jog", "x": 10}
        elif x < -self.threshold:
            return {"command": "jog", "x": -10}
        elif y > self.threshold:
            return {"command": "jog", "y": 10}
        elif y < -self.threshold:
            return {"command": "jog", "y": -10}
        return None

    def get_button_events(self):
        """
        Yield button down events from pygame event queue.

        Yields:
            pygame.event.Event: Button down events.
        """
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                yield event
