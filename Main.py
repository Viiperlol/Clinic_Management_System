from Receptionist import *               # Import all required modules for each user role
from Doctor import *
from Nurse import *
from Patient import *


def main_menu():           # Main menu function to  direct users to their role-specific menus
    while True:
        print("=== Clinic Management System ===")
        print("1. Receptionist")
        print("2. Doctor")
        print("3. Nurse")
        print("4. Patient")
        print("0. Exit")
        choice = input("Select your role: ")

        if choice == '1':
            print("\n" * 20)

            receptionist_menu()
        elif choice == '2':
            print("\n" * 20)
            doctor_menu()
        elif choice == '3':
            print("\n" * 20)
            nurse_menu()
        elif choice == '4':
            print("\n" * 20)
            patient_login_cred()
        elif choice == '0':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
            print("\n" * 10)

main_menu()






