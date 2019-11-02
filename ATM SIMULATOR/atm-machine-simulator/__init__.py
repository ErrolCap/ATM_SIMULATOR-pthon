import msvcrt
from register import registerUser
from crud import retrieve

def main():
    retrieve()

    print("\t\t\t\t\t\t\t=====WELCOME TO THE ATM=====\t\t\t\t\t")
    print("\t\t\t\t\tPlease Select Available Options from below")
    print("[1] Register")
    print("[2] Transaction")
    print("[3] Exit")

    choice = msvcrt.getch().decode('utf-8')

    if choice == '1':
        registerUser()
    elif choice == '2':
        print("bruh")
    elif choice == '3':
        print("bruh")

main()