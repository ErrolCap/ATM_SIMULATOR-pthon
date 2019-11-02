from data import Data
from pinControl import genPin, encrypt
from cardNoGenerator import completed_number
from crud import save, insert, save_to_card
from removableCheck import detect_device, check_removable



def registerUser():
    user = Data
    fname = input("Enter First Name: ")
    mname = input("Enter Middle Name: ")
    lname = input("Enter Last Name: ")
    sex = input("Sex: ")
    pin = genPin()
    print(pin)
    balance = float(input("Enter Balance(Minimum of 500): "))
    while balance < 500:
        print("Insafficient balance, Re-Enter Balance: ")
    cardNo = completed_number(['6','6','6','6'], 16)

    pin = encrypt(pin)

    while detect_device() == 0:
        print("Please insert or re-insert card!")
    path = register_card()


    if insert(user(fname, mname, lname, sex, pin, balance, cardNo)):
        save()
        save_to_card(path, cardNo)

def register_card():
    drive = check_removable("1")

    return drive








