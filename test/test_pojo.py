""" Pojo Unit Test"""
import unittest

from custom_components.ectocontrol.core.model import EctoControlAPIDevice


class MyTestCase(unittest.TestCase):
    """ Pojo Unit Test Cass"""

    def test_device_init(self):
        """ Test Device Pojo construction from Json dict"""
        data = {
            "id": 1,
            "system_object_id": 1,
            "name": "xx",
            "type": "xx"
        }
        device: EctoControlAPIDevice = EctoControlAPIDevice(*data)
        self.assertEqual(device.id, 1)


if __name__ == '__main__':
    unittest.main()
