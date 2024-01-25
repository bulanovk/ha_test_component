"""" API Pojo """
import numbers
from dataclasses import dataclass
from typing import List


@dataclass
class EctoControlAPIDevice:
    """Ectocontrol devices Rest API Pojo"""

    id: numbers
    system_object_id: str
    type: str
    state: str = None
    value: str = None
    name: str = "\"\""

    def __str__(self):
        return f'{self.id}-{self.name}'


@dataclass
class EctoControlAPIDevices:
    """Ectocontrol devices Rest API Pojo"""
    devices: List[EctoControlAPIDevice]

    def __init__(self, devices):
        self.devices = []
        if devices is not None:
            for device in devices:
                self.devices.append(EctoControlAPIDevice(**device))

    def __str__(self):
        return f"{self.devices}"
