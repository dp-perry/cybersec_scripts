#!/usr/bin/env python3

# Read the values of the first 16 registers
# writes the values to file

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
                # Print out to console
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
