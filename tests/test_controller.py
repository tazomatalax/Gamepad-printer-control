import pytest
import pygame
from src.controller import GamepadController

class DummyJoystick:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    def get_axis(self, idx):
        return self._x if idx == 0 else self._y
    def init(self):
        pass

@pytest.fixture(autouse=True)
def patch_pygame(monkeypatch):
    monkeypatch.setattr(pygame, 'init', lambda: None)
    monkeypatch.setattr(pygame.display, 'init', lambda: None)
    monkeypatch.setattr(pygame.joystick, 'get_count', lambda: 1)
    monkeypatch.setattr(pygame.joystick, 'Joystick', lambda idx: DummyJoystick())
    monkeypatch.setattr(pygame.event, 'pump', lambda: None)
    monkeypatch.setattr(pygame.event, 'get', lambda: [])


def test_axis_command_right():
    ctrl = GamepadController()
    ctrl.joystick._x = 1
    ctrl.joystick._y = 0
    assert ctrl.get_axis_command() == {"command": "jog", "x": 10}

def test_axis_command_deadzone():
    ctrl = GamepadController()
    ctrl.joystick._x = 0.1
    ctrl.joystick._y = 0.1
    assert ctrl.get_axis_command() is None

def test_axis_command_left():
    ctrl = GamepadController()
    ctrl.joystick._x = -1
    ctrl.joystick._y = 0
    assert ctrl.get_axis_command() == {"command": "jog", "x": -10}
