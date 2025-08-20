def nurse_menu():
    while True:
        print("\n===  Nurse  ===")
        print("1. See doctor schedules")
        print("2. Record patients observation")
        print("3. Delete patients observation")  # here in this block giving the patients some options to choose from
        print("4. View prescriptions")
        print("5. Give medicine")
        print("6. Back to Main Menu")

        choice = input("Select an option (1-6): ")

        if choice == "1":                      # Call the corresponding function based on the choice
            print("\n" * 20)
            view_doctor_schedules()
        elif choice == "2":
            print("\n" * 20)
            record_patient_observations()
        elif choice == "3":
            print("\n" * 20)
            delete_patient_observations()
        elif choice == "4":
            print("\n" * 20)
            view_prescriptions()
        elif choice == "5":
            print("\n" * 20)
            administer_medicine()
        elif choice == "6":
            print("\n" * 20)
            break
        else:
            print("Error try again!!")


def view_doctor_schedules():
    with open("appointments.txt", "r") as file:
        for line in file:
            print(line)  # will go through the txt file of the appointments and just open the file
    input("Press Enter to continue...")
    print("\n" * 20)


def record_patient_observations():
    try:
        print("PATIENTS LIST:")
        with open("patients.txt", "r") as file:           # Showing existing patients
            for line in file:
                print(line)
        print("\n==================================================\n")
        print("PATIENTS' VITALS LIST:")
        with open("patient_observation.txt", 'r') as file:          # Showing existing patients observations
            for line in file:
                print(line)
        pid_exists = True
        while pid_exists:
            pID = input("Enter patient ID: ").upper()
            pid_exists = False

            with open("patient_observation.txt", "r") as file:
                for line in file:
                    data = line.strip().split(' | ')
                    if data[0] == pID:
                        print("This patient ID already exists. Please enter a unique ID.")    # Error if patient ID not unique
                        pid_exists = True
                        break
                    elif pID == "":
                        print("Please key in a value.")
                        pid_exists = True
                        break

        name = input("Enter name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        temp = input("Enter Temperature: ").upper()  # these are the information the nurse will ask the patients
        pulse = input("Enter Heart rate: ").lower()
        glucose = input("Enter Blood glucose level: ").lower()

        with open("patient_observation.txt", "a") as file:
            file.write(f"{pID} | {name} | {age} | {gender} | {temp} | {pulse} | {glucose}\n")

        print("Patient observations updated.\n")
        print(f"{name} | {age} | {gender} | {temp} | {pulse} | {glucose}\n")          # Save patient observations
        input("Press Enter to continue...")
        print("\n" * 20)

    except Exception as e:
        print(f"Error recording patient observation: {e}")     # Error recording patient observations


def delete_patient_observations():
    print("PATIENTS OBSERVATION LIST:")
    with open("patient_observation.txt", 'r') as file:  # Show all current patient observations
        for line in file:
            print(line)
    try:
        pid_to_delete = input("Enter patient ID to delete: ").strip().upper()
        found = False
        updated_lines = []

        with open("patient_observation.txt", "r") as file:  # Search and delete specific record
            for line in file:
                data = line.strip().split(' | ')
                if data[0] != pid_to_delete:
                    updated_lines.append(line)
                else:
                    found = True

        if found:
            with open("patient_observation.txt", "w") as file:  # deleting patient observations
                file.writelines(updated_lines)
            print(f"Patient with ID {pid_to_delete} has been deleted.")
        else:
            print(f"No patient found with ID {pid_to_delete}.")  # Error if patient ID not found

    except FileNotFoundError:
        print("Error: patient_observation.txt file not found.")  # File not found error
    except Exception as e:
        print(f"An error occurred: {e}")  # Error deleting medical record


def view_prescriptions():
    with open("medical_records.txt", "r") as file:
        for line in file:  # will open the file text file for the records
            print(line)
    input("Press Enter to continue...")


def administer_medicine():
    try:
        print("MEDICAL RECORDS LIST:")
        with open("medical_records.txt", "r") as file:   # Show existing medical records
            for line in file:
                print(line)
        print("\n==================================================\n")
        print("ADMINISTERED PATIENTS LIST:")
        with open("administering_medicine.txt", "r") as file:     #Show existing administration of medicine
            for line in file:
                print(line)

        pid_exists = True
        while pid_exists:
            pID = input("Enter patient ID: ").upper()
            pid_exists = False

            with open("administering_medicine.txt", "r") as file:
                for line in file:
                    data = line.strip().split(" | ")
                    if data[0] == pID:
                        print("This patient ID already exists. Please enter a unique ID.")   # Error if patient ID is not unique
                        pid_exists = True
                        break
                    elif pID == "":
                        print("Please key in a value.")
                        pid_exists = True
                        break

        name = input("Enter patient name: ")
        medicine = input("Enter medicine: ")

        with open("administering_medicine.txt", "a") as file:      # Saving the patient medicine info
            file.write(f"{pID} | {name} |{medicine}\n")

        print("Medicine recorded!")
        input("Press Enter to continue...")
        print("\n" * 20)

    except Exception as e:
        print(f"error administrating medicine: {e}")    # Error administrating medicine


