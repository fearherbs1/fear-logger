# fear-logger
A Keylogging solution written in python. 

# Goals:
1. send encrypted file (rsa) with user keystrokes to remote server
2. along with keystrokes include active window where typing happened
3. randomize key log file name and location in temp dir
4. compile to exe and be unnoticeable when opened. 

# reach goals:
1. some sort of persistence mechanism 
2. have option where log never touches disk and goes straight to server to limit evidence
3. usb mode that would log to usp stick instead of hidden location


# to do:
1. add asci controll characters https://donsnotes.com/tech/charsets/ascii.html
 - most done