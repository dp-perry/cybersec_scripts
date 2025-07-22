from TryHackMe.attackingics2.set_registry import registry

# PyModbus attack scripts
These scripts are updated versions of those originally shared by TryHackMe in their Attacking ICS 1 room.
These scripts work with pymobus==3.9.2 as well as the lab. The originals can be found in the /original folder as a reference.

Also added is an extra check to make sure the correct arguments are given, 
this helps people new to python with how to use the script.

**Usage**
```bash
python3 discovery.py ip_address
python3 set_registry.py ip_address registry value
```

A new script is *discover_to_file.py*, the lab can be unstable making it crash and losing the register data.
This file will write the register data to a file for later reference.

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