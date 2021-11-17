# fear-logger
A simple Key-logging solution written in python.  
I wanted to take a shot at designing some malware, a python keylogger seemed like a good place to start.  
This code is provided for educational purposes only.  

## Features:
- [X] collect keystrokes unknowingly to the user.
- [X] along with keystrokes include the active window where keystrokes happened and note when window is changed
- [X] randomize key log file name.
- [X] encode log in hex to avoid suspicion if log file is found while in operation.
- [X] Support ASCII control characters (ctrl+a)

## Other Ideas:
- [ ] create a small script that converts back to normal text for easy viewing of stolen data.
- [ ] compile to exe and be unnoticeable when opened. (pyinstaller or Nuitka)
- [ ] Undetected by windows Defender
- [ ] save keystrokes to usb stick that script is on.
- [ ] obfuscate code

## Usage:

1. Compile using pyinstaller, Nuitka or Py2win
2. Drop on target system
3. Log files are saved as a random file in the temp dir, for retrieval purposes all files created by this
script end in `_32.txt`
4. Using [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)) or some other tool, convert hex in log file to txt to view data. 