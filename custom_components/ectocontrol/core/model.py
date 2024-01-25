"""" API Pojo """
import numbers
from dataclasses import dataclass, field
from typing import List


@dataclass
class EctoControlAPIDevice:
    """Ectocontrol devices Rest API Pojo"""

    id: numbers
    system_object_id: str
    type: str
    name: str = "\"\""
    state: str = field(default=None)
    value: str = field(default=None)

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
