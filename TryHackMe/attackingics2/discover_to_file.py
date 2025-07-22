#!/usr/bin/env python3

# Modified version of the TryHackMe Modbus discover_to_file.py file
# This version uses pymodbus 3.2 instead of 1.52
# This version writes the output both to a file and the console,
# the virtuaplant can be unstable making it difficult to get a full log.

import sys
import time
from pymodbus.client import ModbusTcpClient

if len(sys.argv) != 2:
    print("Error: Incorrect arguments given")
    print("Usage: ./discover_to_file.py ip_address")
    sys.exit()

ip = sys.argv[1]

client = ModbusTcpClient(ip, port=502)
client.connect()

try:
    with open("modbus_registers.txt", "a") as f:
        while True:
            rr = client.read_holding_registers(1, count=16)
            if not rr.isError():
                # Print output to file
                print(rr.registers, file=f)
                # Pritn out to console
                print(rr.registers)
            else:
                print(f"Error reading registers: {rr}", file=f)
                print(f"Error reading registers: {rr}")
            time.sleep(1)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()
    print("Modbus client closed.")
