#!/usr/bin/python

import smbus
import math

bus = smbus.SMBus(1)
address = 0x77

TEMP_ADD = 0x2E
PRESSURE_ADD = 0xF4

temp = read_word(0x2E)
print temp