import numbers
from typing import List


class EctoControlAPIDevice:
    id: numbers
    system_object_id: str
    name: str
    type: str

    def __init__(self, id, system_object_id, name, type):
        self.id = id
        self.system_object_id = system_object_id
        self.name = name
        self.type = type


class EctoControlAPIDevices:
    devices: List[EctoControlAPIDevice]

    def __init__(self, devices):
        self.devices = []
        for device in devices:
            self.devices.append(EctoControlAPIDevice(**device))