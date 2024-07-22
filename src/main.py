from exploits import *
from helpers import *

# This is a menu for the exploits that I will be testing on the metasploitable 2 machine
def dispMenu():
    exploits = ["Samba", "UnrealIRCd", "VSFTP", "SSH Brute Force", "Distccd"]

    for index, item in enumerate(exploits, start=1):
        print(f"({index}) {item}")
    print("(0) Exit")

# This handles the menu option that is selected
def optionHandler(selection, rHost, lHost):
    try:
        choice = int(selection)
    except ValueError:
        print("Error: Please enter a valid number.")
        return True  

    if choice == 1:
        exploitSamba(rHost, lHost)
    elif choice == 2:
        exploitUnrealIRCd(rHost,lHost)
    elif choice == 3:
        exploitVSFTP(rHost)
    elif choice == 4:
        exploitBruteForce(rHost)
    elif choice == 5:
        exploitDistccd(rHost, lHost)
    elif choice == 0:
        print("Exiting...")
        return False  
    else:
        print("Error: Selection out of range. Please try again")
    return True  


if __name__ == "__main__":
    
    lHost = input(f"Enter your IP Address: ")
    
    rHost = input(f"Enter targets IP Address: ")

    print(f"Select an exploit to run. Select '0' to quit.")

    while True:
        
        dispMenu()
        
        selection = input("Enter exploit option: ")
        if not optionHandler(selection, rHost, lHost):
            break
        

        
