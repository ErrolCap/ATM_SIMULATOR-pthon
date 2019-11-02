import os, string, time
from ctypes import windll

def get_driveStatus():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()

    for label in range(26):
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices


def detect_device():
    original = set(get_driveStatus())
    time.sleep(2)
    add_device = set(get_driveStatus()) - original
    if (len(add_device)):
        for drive in add_device:

            return drive + 65
    else:
        return 0

def detect_remove():
    original = set(get_driveStatus())
    time.sleep(2)
    subt_device = original - set(get_driveStatus())
    if (len(subt_device)):
        for drive in subt_device:
            return drive + 65
    else:
        return 0

def check_removable(mode):
        while True:
            drive = detect_device()
            if drive != 0:
                return chr(drive)

    else:
        while True:
            drive = detect_remove()
            if drive != 0:
                return drive