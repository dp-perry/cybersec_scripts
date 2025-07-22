# PyModbus attack scripts
Example scripts for attacking the Virtuaplant in the TryHackMe Attacking ICS 2 room
These scripts work with pymobus==3.9.2 as well as the lab.

**Usage**
```bash
python3 discovery.py ip_address
python3 set_registry.py ip_address registry value
python3 attack_oil_tank.py ip_address
```

### Creating a virtual enviroment
I personally like to create a virtual environment for projects to keep packages contained to a single project.
This can prevent issues when certain projects or attack depend on a specific package version. Below is my process.
```bash
# Create a new environment 
python -m venv ics-env
# Activate the enviroment
source ics-env/bin/activate
# Install the required packages
pip install -r requirements.txt
# OR install a package manually 
pip install pymodbus==3.9.2
```