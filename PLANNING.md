# Project Planning

## 🚀 Vision & Purpose
Enable intuitive, real-time control of an OctoPrint-enabled 3D printer using a gamepad or joystick, making printer operation more accessible and interactive.

## 🏗️ Architecture
- Modular Python application
- Input Layer: Reads gamepad/joystick input via pygame (controller.py)
- API Layer: Sends commands to OctoPrint REST API (octoprint_client.py)
- Main Loop: Orchestrates input and API calls (main.py)
- Config: Uses environment variables for OctoPrint connection
- Tests: Pytest-based unit tests in /tests

## 🛠️ Tech Stack
- Language: Python 3
- Frameworks: None (CLI app)
- Libraries: pygame, requests, python-dotenv, pytest
- Database: None
- Other Tools: OctoPrint server, gamepad/joystick hardware

## 🧩 Components
- src/controller.py: Handles gamepad/joystick input
- src/octoprint_client.py: Handles OctoPrint API communication
- src/main.py: Entry point and event loop
- /tests: Unit tests for all modules

## 🔍 Constraints & Requirements
- Must support Xbox-style controllers (via pygame)
- Must not exceed 500 lines per file (modular design)
- All configuration via environment variables
- No persistent storage required
- Code must be PEP8 compliant and well-documented

## 📏 Code Style & Conventions
- PEP8 formatting
- Type hints required
- Google-style docstrings for all functions/classes
- Use relative imports within src/
- Tests must cover expected, edge, and failure cases

## 🗺️ Project Roadmap
1. Modularize codebase (done)
2. Add unit tests (done)
3. Improve error handling and logging
4. Add support for custom button mapping via config file
5. Optional: GUI for configuration

## 📚 References
- [Pygame Joystick Docs](https://www.pygame.org/docs/ref/joystick.html)
- [OctoPrint REST API](https://docs.octoprint.org/en/master/api/)
- [requests library](https://docs.python-requests.org/en/latest/)
- [pytest](https://docs.pytest.org/en/stable/)
