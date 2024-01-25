"""" API Pojo """
import numbers
from dataclasses import dataclass
from typing import List, Any
import re


@dataclass
class EctoControlAPIDevice:
    """Ectocontrol devices Rest API Pojo"""

    id: numbers
    system_object_id: str
    type: str
    state: str = None
    value: str = None
    name: str = ""
    signal_level: str = 0
    system_firmware_version: str = None
    connection: bool = True

    def __str__(self):
        return f'{self.id}-{self.name}'

    def __post_init__(self):
        if self.name is not None:
            self.name = re.sub('"(.*)"$', '\\1', self.name)

    def update(self, data: dict[str, Any]):
        for key, value in data.items():
            self.__setattr__(key, value)
        if self.name is not None:
            self.name = re.sub('"(.*)"$', '\\1', self.name)


@dataclass
class EctoControlAPIDevices:
    """Ectocontrol devices Rest API Pojo"""
    devices: dict[str, EctoControlAPIDevice]

    def __init__(self, devices):
        self.devices = {}
        if devices is not None:
            for device in devices:
                self.devices[device.get("id")] = EctoControlAPIDevice(**device)

    def __str__(self):
        return f"{self.devices}"
