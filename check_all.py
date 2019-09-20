#!/usr/bin/python

import broadlink

devices = broadlink.mp1(host=('192.168.1.2', 80), mac=bytearray.fromhex('78 0F 77 59 43 4A'), devtype='mp1')
devices.auth()

print devices.check_power()

