#!/usr/bin/python

import broadlink

devices = broadlink.discover(timeout=5)
devices[0].auth()
puts devices[0]

