import re
import subprocess
import requests
from typing import List

# Regulärer Ausdruck zum Testen von IP-Adressen
re_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

# Standardport, der zum Auffinden der Netwerkgeräte verwendet werden soll
STD_PORT = 80


class NetworkDevice():

    def __init__(self, ip_address: str, port: int = STD_PORT):
        self.ip_address = ip_address
        self.port = port

    @classmethod
    def all(cls) -> List['SmartNetworkDevice']:
        """
        Finde alle Netwerkgeräte, die mit diesem Geräte kommuniziert haben

        :returns: Liste von Netwerkgeräten
        :rtype: List
        """
        output = subprocess.check_output(
            "arp -n | awk '{print $1}'", shell=True).decode('utf-8')

        devices = []
        rows = output.split('\n')
        for row in rows:
            ip_address = str(row)
            if not re_ip.match(ip_address.strip()):
                continue
            devices.append(NetworkDevice(ip_address))

        return devices

    def to_dict(self):
        return {
            "ip_address": self.ip_address,
            "port": self.port,
        }
