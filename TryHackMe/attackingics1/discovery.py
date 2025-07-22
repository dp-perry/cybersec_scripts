#!/usr/bin/env python3

# Modified version of the TryHackMe Modbus discovery.py file
# This version uses pymodbus 3.2 instead of 1.52

import sys
import time
from pymodbus.client import ModbusTcpClient

if len(sys.argv) != 2:
    print("Error: Incorrect arguments given")
    print("Usage: ./discovery.py ip_address")
    sys.exit()

ip = sys.argv[1]

client = ModbusTcpClient(ip, port=502)
client.connect()

while True:
    rr = client.read_holding_registers(1, count=16)
    print(rr.registers)
    time.sleep(1)
