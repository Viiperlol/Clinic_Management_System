import os                                                     #import the OS Module

def patient_login_cred():                    #To input ID to log in                                       #Exit the menu and return to main.py
    pid_exists = True
    while pid_exists:
        patient_id = input("Enter patient ID: ").upper()
        pid_exists = False

    password_exists = True                   #To input password to log in
    while password_exists:
        password = input("Enter Password: ")
        password_exists = False

        def patient_log_in_process():                          #to read the text file and check if the ID and password exists
            try:
                found = False
                with open("patients.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(' | ')
                        # print(data)
                        if data[0] == patient_id and data[5] == password:
                            found = True
                    if found:                                  #if ID and password exist, the user is logged in to main menu
                        print("\n" * 20)
                        print("Login successful, Welcome")
                        patient_menu()
                    else:                                      #if they don't exist
                        print("\n"*20)
                        print("Patient ID was not found")
                        os.system("main.py")


            except Exception as e:
                print(f"error logging in: {e}")    #if cannot read file, handle error


        def patient_menu():
            while True:
                print("=== Patient System ===")
                print("1. View Medical Records")
                print("2. View Appointments")
                print("3. Add Personal Information")
                print("4. Update Personal Information")
                print("5. View Billing and Payment information")
                print("6. Give Feedback")
                print("7. Exit")
                choice = input("Enter a choice: ")

                if choice == "1":                              #call menu option based on users choice
                    print("\n" * 20)
                    view_medical_records()
                elif choice == "2":
                    print("\n" * 20)
                    view_appointments()
                elif choice == "3":
                    print("\n" * 20)
                    add_personal_information()
                elif choice == "4":
                    print("\n" * 20)
                    update_personal_information()
                elif choice == "5":
                    print("\n" * 20)
                    view_billing_and_payment_information()
                elif choice == "6":
                    print("\n" * 20)
                    give_feedback()
                elif choice == "7":
                    print("Exiting the Menu!")
                    print("\n" * 20)
                    return                       #Exit the menu and return to main.py
                else:                                            #for invalid choices
                    print("Invalid Option. Try Again.")
                    print("\n" * 10)


        def view_medical_records():                              #function to view medical records
            print("\n"*20)
            try:
                with open("medical_records.txt", "r") as file:
                    found = False
                    for line in file:
                        data = line.strip().split(" | ")         #to rearrange the data into strip style
                        # print(data)
                        if data[0] == patient_id:
                            found = True
                            pID = data[0].strip()
                            Name = data[1].strip()
                            Age = data[2].strip()
                            Gender = data[3].strip()
                            Diagnosis = data[4].strip()
                            Prescription = data[5].strip()
                            Treatment_plans = data[6].strip()
                            Specialization = data[7].strip()

                    if found:                                      #if the data is found, then print the following
                        print("---- Patient Medical Record ----")
                        print(f"Patient ID      : {pID}")
                        print(f"Name            : {Name} ")
                        print(f"Age             : {Age}")
                        print(f"Gender          : {Gender}")
                        print(f"Diagnosis       : {Diagnosis}")
                        print(f"Prescription    : {Prescription}")
                        print(f"Treatment plans : {Treatment_plans}")
                        print(f"Specialization  : {Specialization} ")
                        input("\nPress Enter to continue...")
                        print("\n"*20)
                    else:
                        print("The Patient Medical Record was not Found")
            except Exception as e:                                  #if the file wasn't found to view
                print(f"error viewing medical records: {e}")


        def view_appointments():                                    #Function to view appointment details
            try:
                with open("appointments.txt", "r") as file:
                    found = False
                    for line in file:
                        data = line.strip().split(" | ")
                        if data[0] == patient_id:
                            found = True

                    if found:                                       #if data is found, print the following
                        print("Your next appointment is on ", data[5])
                        input("Press Enter to continue...\n")
                        print("\n"*20)
                    else:
                        print("No more appointments, thank you")

            except Exception as e:                                 #if the file wasn't found to view
                print(f"error viewing appointments: {e}")

        def add_personal_information():
            try:
                pID = patient_id
                with open("patients_personal_information.txt", "r") as file:            # Check if patient ID already exists
                    for line in file:
                        if line.strip().split(' | ')[0] == pID:
                            print("This patient ID already exists. Please enter a unique ID.\n\n")   # Redirects to patient menu if ID exists
                            return

                pID = patient_id                                        # Gather patient information from user
                name = input("Enter name: ")
                contact = input("Enter contact number: ")
                address = input("Enter your address: ")

                with open("patients_personal_information.txt", "a") as file:           # Input new patient record to the file
                    file.write(f"{pID} | {name} | {contact} | {address}\n")

                print("Patient registered successfully.\n")
                input("Press Enter to continue...")
                print("\n" * 20)
            except Exception as e:
                print(f"Error registering patient: {e}")          #if the file wasn't found to view


        def update_personal_information():                         #Function to update personal information
            try:
                pID = patient_id
                found = False
                with open("patients_personal_information.txt", "r") as file:     # Read all existing patient records
                    lines = file.readlines()

                with open("patients_personal_information.txt", "w") as file:    # Reopen the file in write mode to put updated records
                    for line in lines:
                        data = line.strip().split(" | ")
                        if data[0] == pID:
                            found = True             # if patient was found, get new information and put it in the text file
                            name = input("Enter new name: ")
                            contact = input("Enter new contact number: ")
                            address = input("Enter new address: ")
                            file.write(f"{pID} | {name} | {contact} | {address}\n")
                        else:                      # Keep the existing record unchanged
                            file.write(line)

                if found:                   # Notify the user about the result
                    print("Patient information updated successfully.")
                    input("Press Enter to continue...")
                    print("\n" * 20)
                else:
                    print("Patient ID not found.")
            except FileNotFoundError:                   #if the file wasn't found to view
                print("The Patient Personal Information File Was Not Found")


        def view_billing_and_payment_information():                #Function to view billing and payment info of the patient
            try:
                pID = patient_id
                found = False
                with open("payments.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(" | ")
                        if data[0] == pID:                         #To see if first data matches with patient ID or not
                            pID = data[0].strip()
                            Amount = data[1].strip()
                            Payment_method = data[2].strip()
                            found = True

                    if found:                                     #if the data matches
                        print("--- Patient Payment Information ---")
                        print(f"Patient ID:       {pID}")
                        print(f"Payment Amount:   {Amount}")
                        print(f"Payment Method:   {Payment_method}\n")
                        input("Press Enter to continue...")
                        print("\n" * 20)
                    else:                                         #if not
                        print("Your Payment Information Not Found")
            except Exception as e:                                #if the file was not found to view
                print(f"error viewing payment information: {e}")


        def give_feedback():                                     #Function to give Feedback
            pID = patient_id
            Name = input("Enter Name: ")
            print("1  2  3  4  5")
            Rating = int(input("Choose a Number from 1 to 5: ")) #To give rating out of 5 and comment
            Comment = input("Enter a Feedback Comment: ")

            with open("Feedback.txt", "a")as file:
                file.write(f"{pID} | {Name} | {Rating} Star Rating | {Comment}\n")  #save feedback data to file
            print("\n" * 20)
            print("Feedback updated successfully.")

        patient_log_in_process()   #Call the login processing function once inputs are collected