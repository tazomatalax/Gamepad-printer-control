"""
octoprint_client.py

Handles communication with the OctoPrint API.
"""
import requests
from typing import Dict, Any

class OctoPrintClient:
    """
    Client for sending commands to OctoPrint API.
    """
    def __init__(self, ip: str, port: str, api_key: str):
        """
        Initialize the OctoPrint client.

        Args:
            ip (str): OctoPrint server IP.
            port (str): OctoPrint server port.
            api_key (str): OctoPrint API key.
        """
        self.url = f"http://{ip}:{port}/api/printer/printhead"
        self.api_key = api_key

    def send_command(self, command: Dict[str, Any]) -> bool:
        """
        Send a command to the OctoPrint API.

        Args:
            command (Dict[str, Any]): Command payload.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            response = requests.post(self.url, json=command, headers={'X-Api-Key': self.api_key})
            if response.status_code == 204:
                print('Request was successful:', command)
                return True
            else:
                print('Request failed. Status code:', response.status_code, command)
                return False
        except Exception as e:
            print('Error sending request:', e)
            return False
