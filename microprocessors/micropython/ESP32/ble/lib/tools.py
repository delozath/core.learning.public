# This example demonstrates a UART periperhal.

import bluetooth
import struct

from micropython import const

_ADV_TYPE_FLAGS = const(0x01)
_ADV_TYPE_NAME = const(0x09)
_ADV_TYPE_UUID16_COMPLETE = const(0x3)
_ADV_TYPE_UUID32_COMPLETE = const(0x5)
_ADV_TYPE_UUID128_COMPLETE = const(0x7)
_ADV_TYPE_UUID16_MORE = const(0x2)
_ADV_TYPE_UUID32_MORE = const(0x4)
_ADV_TYPE_UUID128_MORE = const(0x6)
_ADV_TYPE_APPEARANCE = const(0x19)


class Payload():
    def __init__(self, limited_disc=False, br_edr=False, name=None, services=None, appearance=0):
        self._payload = bytearray()
        self._append(_ADV_TYPE_FLAGS,
                      struct.pack("B", 
                                  (0x01 if limited_disc else 0x02) + (0x18 if br_edr else 0x04)
                                 )
                    )
        if name:
            self._append(_ADV_TYPE_NAME, name)
        #
        if services:
            self._set_services(services)
        #
        # See org.bluetooth.characteristic.gap.appearance.xml
        if appearance:
            self._append(_ADV_TYPE_APPEARANCE, struct.pack("<h", appearance))
    #
    def get(self):
        return self._payload     
    #
    def _append(self, adv_type, value):
        self._payload += struct.pack("BB", len(value) + 1, adv_type) + value
    #
    def _set_services(self, services):
        for uuid in services:
            b = bytes(uuid)
            if len(b) == 2:
                self._append(_ADV_TYPE_UUID16_COMPLETE,  b)
            elif len(b) == 4:
                self._append(_ADV_TYPE_UUID32_COMPLETE,  b)
            elif len(b) == 16:
                self._append(_ADV_TYPE_UUID128_COMPLETE, b)