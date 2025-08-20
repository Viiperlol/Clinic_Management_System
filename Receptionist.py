# Menu
def receptionist_menu():
    while True:
        print("\n=== Receptionist System ===")     # Prints the options for receptionist menu
        print("1. Register new patient")
        print("2. Delete patient detail")
        print("3. Update patient detail")
        print("4. Schedule appointment")
        print("5. Delete appointment")
        print("6. Process payment and receipt")
        print("7. View patient feedback")
        print("8. Back to main menu")

        choice = input("Select an option (1-8): ")

        if choice == '1':                           # Have a choice for every option which will
            print("\n" * 20)                        # link to the function
            register_patient()
        elif choice == '2':
            print("\n" * 20)
            delete_patient()
        elif choice == '3':
            print("\n" * 20)
            update_patient_detail()
        elif choice == '4':
            print("\n" * 20)
            schedule_appointment()
        elif choice == '5':
            print("\n" * 20)
            delete_appointment()
        elif choice == '6':
            print("\n" * 20)
            payment()
        elif choice == '7':
            print("\n" * 20)
            patient_feedback()
        elif choice == '8':
            print("Going to main menu...")              # If an invalid choice is given,
            print("\n"*20)                              # ask the user again
            break
        else:
            print("Invalid selection. Please try again.")

# Register new patients into the system.
def register_patient():
    print("PATIENTS' LIST:")
    with open("patients.txt", 'r') as file:             # Open patient's file
        for line in file:
            print(line)                                 # Print every line from the
    try:                                                # txt file into the console
        pid_exists = True
        while pid_exists:
            pID = input("Enter patient ID: ").upper()   # Keep asking the user for input
            pid_exists = False                          # until a unique ID is given

            # Check if patient ID already exists
            with open("patients.txt", "r") as file:         # convert the txt into a list
                for line in file:                           # read index 0 (ID index) and
                    if line.strip().split(' | ')[0] == pID: # compare to input
                        print("This patient ID already exists. Please enter a unique ID.")
                        pid_exists = True
                        break
                    elif pID == "":
                        print("Please key in a value.")
                        pid_exists = True
                        break

        name = input("Enter patient name: ")                # if input == index 0,
        age = (input("Enter age: "))                        # ask for patient details
        gender = input("Enter gender: ")
        condition = input("Enter medical condition: ")
        key = name+age

        with open("patients.txt", "a") as file:  # write the inputs into a new line in txt file
            file.write(f"{pID} | {name} | {age} | {gender} | {condition} | {key}\n")

        print("Patient registered successfully.\n")
        input("Press Enter to continue...")
        print("\n" * 20)
    except Exception as e:
        print(f"Error registering patient: {e}")

def delete_patient():
    print("PATIENTS' LIST:")
    with open("patients.txt", 'r') as file:
        for line in file:
            print(line)
    try:
        pid_to_delete = input("Enter patient ID to delete: ").strip()
        found = False               # set found = False as a placeholder
        updated_lines = []          # create an empty list

        with open("patients.txt", "r") as file:
            for line in file:
                data = line.strip().split(' | ')
                if data[0] != pid_to_delete:        # if input does not match the index 0,
                    updated_lines.append(line)      # append the txt file into the empty list
                else:
                    found = True                    # if input does match the index 0,
                                                    # set found = true
        if found:
            with open("patients.txt", "w") as file: # it will write an empty line deleting
                file.writelines(updated_lines)      # the prev patient
            print(f"Patient with ID {pid_to_delete} has been deleted.\n")
            input("Press Enter to continue...")
            print("\n" * 20)
        else:
            print(f"No patient found with ID {pid_to_delete}.")

    except FileNotFoundError:
        print("Error: patients.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Update patients' details.
def update_patient_detail():
    try:
        with open("patients.txt", 'r') as file:
            for line in file:
                print(line)
        pID = input("\nEnter patient ID to update: ").upper()
        updated_lines = []
        found = False
        with open("patients.txt", "r") as file:
            for line in file:
                data = line.strip().split(' | ')
                # print(data)
                if data[0] == pID:
                    found = True
                    name = input("Enter new name: ")
                    age = (input("Enter age: "))
                    gender = input("Enter gender: ")
                    condition = input("Enter medical condition: ")
                    key = name+age
                    updated_lines.append(f"{pID} | {name} | {age} | {gender} | "
                                         f"{condition} | {key}\n")
                else:
                    updated_lines.append(line)

        if found:
            with open("patients.txt", "w") as file:
                file.writelines(updated_lines)
            print("Patient details updated.\n")
            input("Press Enter to continue...")
            print("\n" * 20)
        else:
            print("\nPatient ID not found.\n")
            update_patient_detail()
    except Exception as e:
        print(f"Error updating details: {e}")


# Schedule appointments for patients.
def schedule_appointment():
    print("PATIENTS LIST:")
    with open("patients.txt", 'r') as file:
        for line in file:
            print(line)
    print("\n==================================================\n")
    print("DOCTOR'S SCHEDULE LIST:")
    with open("doctor_schedule.txt", 'r') as file:
        for line in file:
            print(line)
    print("\n==================================================\n")
    print("APPOINTMENTS LIST:")
    with open("appointments.txt", 'r') as file:
        for line in file:
            print(line)
        print("\n")

    try:
        # Validate patient ID
        valid_id = False
        while not valid_id:
            pID = input("Enter patient ID to schedule: ").upper()

            if pID == "":
                print("Patient ID cannot be empty. Please try again.")
                continue

            with open("patients.txt", 'r') as file:
                for line in file:
                    patient_id = line.strip().split(' | ')[0]
                    if patient_id == pID:
                        valid_id = True
                        break

            if not valid_id:
                print("Error: Patient ID not found. Please enter a valid existing ID.")

        # Continue with appointment scheduling
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        condition = input("Enter medical condition: ")
        date = input("Enter appointment day: ")

        with open("appointments.txt", "a") as file:
            file.write(f"{pID} | {name} | {age} | {gender} | {condition} | {date}\n")

        print("Appointment scheduled.")
        print(f"{pID} | {name} | {age} | {gender} | {condition} | {date}\n")
        input("Press Enter to continue...")
        print("\n" * 20)

    except Exception as e:
        print(f"Error scheduling appointment: {e}")


def delete_appointment():
    print("APPOINTMENTS' LIST:")
    with open("appointments.txt", 'r') as file:
        for line in file:
            print(line)
    try:
        pid_to_delete = input("Enter patient ID to delete: ").strip()
        found = False
        updated_lines = []

        with open("appointments.txt", "r") as file:
            for line in file:
                data = line.strip().split(' | ')
                if data[0] != pid_to_delete:
                    updated_lines.append(line)
                else:
                    found = True

        if found:
            with open("appointments.txt", "w") as file:
                file.writelines(updated_lines)
            print(f"Patient with ID {pid_to_delete} has been deleted.")
        else:
            print(f"No patient found with ID {pid_to_delete}.")

    except FileNotFoundError:
        print("Error: patients.txt file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Process payments and generate receipts for patients.
def payment():
    print("PATIENTS LIST:")
    with open("patients.txt", 'r') as file:
        for line in file:
            print(line)
    print("\n==================================================\n")
    print("SERVICE CHARGES LIST:")
    print("Eye service: $25\n")
    print("Eye medicine: $50\n")
    print("Skin service: $15\n")
    print("Skin medicine: $25\n")
    print("Ear service: $15\n")
    print("Ear medicine: $10\n")
    print("General service: $20\n")
    print("General medicine: $10\n")
    print("\n==================================================\n")
    print("PAYMENTS ADMINISTERED:")
    try:
        with open("payments.txt", "r") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("Note: payments.txt not found. It will be created after adding payment.\n")

    try:
        # Validate patient ID is not empty and not already in payments.txt
        valid_id = False
        while not valid_id:
            pID = input("Enter patient ID: ").strip().upper()

            if pID == "":
                print("Patient ID cannot be empty. Please try again.")
                continue

            id_exists = False
            try:
                with open("payments.txt", "r") as file:
                    for line in file:
                        existing_id = line.strip().split(' | ')[0]
                        if existing_id == pID:
                            id_exists = True
                            break
            except FileNotFoundError:
                pass  # If file doesn't exist yet, it's okay

            if id_exists:
                print("This patient ID already has a payment record. "
                      "Please enter a different ID.")
            else:
                valid_id = True

        # Continue with payment details
        condition = input("Enter patient's condition: ").lower()
        if condition == "eye":
            amount = "$75"
        elif condition == "skin":
            amount = "$40"
        elif condition == "ear":
            amount = "$35"
        elif condition == "general":
            amount = "$30"
        else:
            amount = "$0"

        method = input("Enter payment method: ")

        with open("payments.txt", "a") as file:
            file.write(f"{pID} | {amount} | {method}\n")

        print(f"Payment processed. The payment amount is {amount}\n")
        input("Press Enter to continue...")
        print("\n" * 20)

    except Exception as e:
        print(f"Error processing payment: {e}")

def patient_feedback():
    print("PATIENTS' FEEDBACK:")
    try:
        with open("Feedback.txt", "r") as file:
            for line in file:
                print(f"{line}")
            print("\n")
            input("Press Enter to continue...")
            print("\n" * 20)
    except FileNotFoundError:
        print("No feedback available yet. Please add feedback first.\n")