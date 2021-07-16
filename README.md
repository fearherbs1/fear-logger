# fear-logger
A Keylogging solution written in python.  
The purpose of this is project to experiment writing some malware.

# Goals:
## 2 versions
### Static Version
This version would be used when physical access  is possible.
The script can be loaded on an usb stick, dropped on a forgotten about un-locked computer, and save
keystrokes to that usb stick. The usb stick can then be later recovered to grab the data.

This version will be a lot less "noisy" as there is no network traffic involved nor persistence mechanism.  
The keylog file will also never touch the disk and only the usb drive that it is stored on.

- [X] collect keystrokes unknowingly to the user.
- [X] along with keystrokes include the active window where typing happened and note when window is changed
- [X] randomize key log file name.
- [X] encode log in hex to avoid suspicion if log file is found while in operation.
- [ ] create a small script that converts back to normal text for easy viewing of stolen data.
- [ ] compile to exe and be unnoticeable when opened. (pyinstaller or Nuitka)
- [ ] Undetected by windows Defender
- [ ] save keystrokes to usb stick that script is on.
- [ ] obfuscate code

### Server / Client Version
- [ ] The same general concept as static version, but using sockets to write keystrokes to a remote server.  
this will keep all keystrokes from touching the disk and producing forensic artifacts.
- [ ] incorporate encryption between the client and server
- [ ] some sort of persistence mechanism 

# other to do:
- [x] add asci control characters https://donsnotes.com/tech/charsets/ascii.html
