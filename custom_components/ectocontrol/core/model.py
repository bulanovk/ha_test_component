"""" API Pojo """
import numbers
from dataclasses import dataclass
from typing import List


@dataclass
class EctoControlAPIDevice:
    """Ectocontrol devices Rest API Pojo"""

    id: numbers
    system_object_id: str
    name: str
    type: str

    def __init__(self, id, system_object_id, name, type): # pylint: disable=redefined-builtin
        self.id = id
        self.system_object_id = system_object_id
        if name is not None:
            self.name = name[1:-1]
        self.type = type

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
