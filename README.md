# Collection of scripts used in Cybersecurity labs
This repo contains a collection of scripts used in Cybersecurity labs, 
some are specific to a lab, and some can be reused in different labs / CTFs.


## Platforms
A portion of the scripts will be lab-specific, these will be sorted in Platform / Lab folders.


## Currently contains
- TryHackMe
    - Directory DFIR
    - Attacking ICS 1 & 2
- PyModbus

## General advise
For those new to Python here are some tips, especially if you are working on a Windows machine.

### Running Python scripts
Depending on how Python is installed, you may need to try some different ways of running the script. Below are some examples:
```bash
python script.py arguments
python3 script.py arguments
py script.py arguments
```

I would personally also highly recommend you use virtual environment; this is especially useful when using scripts
written by other people. This will prevent issues with versions if a script depends on a specific version.
```bash
# Create a new environment 
python -m venv py-env
# Activate the enviroment
source py-env/bin/activate
# Install the required packages
pip install -r requirements.txt
# OR install a package manually, for example pwntools
pip install pwntools
# Don't forget to deactivate when switching projects 
deactivate
```