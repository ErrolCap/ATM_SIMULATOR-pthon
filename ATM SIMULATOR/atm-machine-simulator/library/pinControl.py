import random


def genPin():
    pin = ""
    for i in range(6):
        pin += str(random.randint(0,9))

    return pin

def encrypt(pin):
    pin = list(pin)
    pin2 = ''
    for i in range (0, len(pin)):
        x = chr(ord(pin[i]) + 30)
        pin2 += str(x)

    return pin2

def decrypt(pin):
    pin = list(pin)
    pin2 = ''
    for i in range (0, len(pin)):
        x = chr(ord(pin[i]) - 30)
        pin2 += str(x)

    return pin2