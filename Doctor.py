def doctor_menu():                  # Doctor's Main Menu which allows doctors to access all functionalities
    while True:
        print("\n=== Doctors Menu ===")
        print("1. View Patients Medical Record")
        print("2. Create Medical Record")
        print("3. Update Medical Record")
        print("4. Delete patient record")
        print("5. View Appointments")
        print("6. Block/Unblock Availability")
        print("7. Back to Main Menu")

        choice = input("Select an option (1-7): ")

        if choice == '1':                              # Call the corresponding function based on the choice
            print("\n" * 20)
            view_medical_record()
        elif choice == '2':
            print("\n" * 20)
            create_medical_record()
        elif choice == '3':
            print("\n" * 20)
            update_medical_record()
        elif choice == '4':
            print("\n" * 20)
            delete_patient()
        elif choice == '5':
            print("\n" * 20)
            view_doctor_appointments()
        elif choice == '6':
            print("\n" * 20)
            block_unblock_availability()
        elif choice == '7':
            print("\n" * 20)
            break                                      # Return to main menu
        else:
            print("Invalid choice. Try again.")


def view_medical_record():                             #Function to view all patient medical records from file
    print("MEDICAL RECORDS LIST:")
    with open ("medical_records.txt", "r") as file:    #Open medical records to read
        for line in file:
            print(line)
    input("Press Enter to continue...")
    print("\n" * 20)

def create_medical_record():                          # Function to create a new patient medical record
    global pID
    try:
        print("PATIENTS LIST:")
        with open("patients.txt", 'r') as file:       # Display existing patients
            for line in file:
                print(line)
        print("\n==================================================\n")
        print("MEDICAL RECORDS LIST:")
        with open("medical_records.txt") as file:     # Display existing medical records
            for line in file:
                print(line)

        pid_exists = True                             # Ensure unique patient ID entry
        while pid_exists:
            pID = input("Enter patient ID: ").upper()
            pid_exists = False

            with open("medical_records.txt", "r") as file:
                for line in file:
                    data = line.strip().split(' | ')
                    if data[0] == pID:
                        print("This patient ID already exists. Please enter a unique ID.")  # Error if patient ID already exist
                        pid_exists = True
                        break
                    elif pID == "":
                        print("Please key in a value.")    # Error if no value is keyed in
                        pid_exists = True
                        break

        name = input("Enter patient name: ")                    # Collect medical details
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: ")
        diagnosis = input("Enter diagnosis: ")
        prescription = input("Enter prescription: ")
        treatment_Plans = input("Enter treatment plan: ")
        specialization = input("Enter your specialization (Eye/Skin/Ear/General): ")

        with open("medical_records.txt", "a") as file:           # Enter new record to medical records file
            file.write(f"{pID} | {name} | {age} | {gender} | {diagnosis} | "
                       f"{prescription} | {treatment_Plans} | {specialization}\n")

        print("Medical Record created.\n")
        input("Press Enter to continue...")
        print("\n" * 20)
    except Exception as e:
        print(f"Error creating medical record : {e}")        #Error creating medical record


def update_medical_record():                           # Function to update an existing medical record
    try:
        with open ("medical_records.txt", "r") as file:    # Show all current medical records
            for line in file:
                print(line)

        pID = input("Enter patient ID to update: ").strip().upper()   #Ensure patient ID exists
        updated_lines = []
        found = False
        with open("medical_records.txt", "r") as file:    # Search and update the specific record
            for line in file:
                data = line.strip().split(" | ")
                if data[0] == pID:
                    found = True
                    pID = input ("Enter new patient ID: ").upper()   #Enter updated data
                    Name = input("Enter new name: ")
                    Age = input("Enter new age: ")
                    Gender = input("Enter gender: ")
                    Diagnosis = input("Enter diagnosis: ")
                    Prescription = input("Enter prescription: ")
                    Treatment_Plans = input("Enter treatment plans: ")
                    Specialization = input("Enter specialization: ")
                    updated_lines.append(f"{pID} | {Name} | {Age} | {Gender} | {Diagnosis} "
                                         f"| {Prescription} | {Treatment_Plans} | {Specialization}\n")
                else:
                    updated_lines.append(line)

        if found:                                               # Save updated records back to file
            with open("medical_records.txt", "w") as file:
                file.writelines(updated_lines)
            print("Medical report updated")
            input("Press Enter to continue...")
            print("\n" * 20)
        else:
            print("\nPatient ID not found")            # Error if patient ID not found
            update_medical_record()
    except Exception as e:
            print(f"Error uploading medical details; {e}")     #Error updating medical record


def delete_patient():                # Function to delete a patient’s medical record
    print("PATIENTS MEDICAL RECORDS LIST:")
    with open("medical_records.txt", 'r') as file:       # Show all current medical records
        for line in file:
            print(line)
    try:
        pid_to_delete = input("Enter patient ID to delete: ").strip().upper()
        found = False
        updated_lines = []

        with open("medical_records.txt", "r") as file:       # Search and delete specific record
            for line in file:
                data = line.strip().split(' | ')
                if data[0] != pid_to_delete:
                    updated_lines.append(line)
                else:
                    found = True

        if found:
            with open("medical_records.txt", "w") as file:     # Save and update medical records
                file.writelines(updated_lines)
            print(f"Patient with ID {pid_to_delete} has been deleted.")
        else:
            print(f"No patient found with ID {pid_to_delete}.")    # Error if patient ID not found

    except FileNotFoundError:
        print("Error: medical_records.txt file not found.") # File not found error
    except Exception as e:
        print(f"An error occurred: {e}")      # Error deleting medical record


def view_doctor_appointments():                    # Function to view doctor's appointment list
    print("APPOINTMENTS LIST:")
    with open ("appointments.txt", "r") as file:   # Open appointment record to read
        for line in file:
           print(line)


def block_unblock_availability():    # Function to block or unblock doctor's availability for specific days
    print("\n" * 20)
    try:
        with open("doctor_schedule.txt", 'r') as file:     # Show current doctor availability
            for line in file:
                print(line)
        day = input("\nChange availability for which day: ").capitalize()
        updated_lines = []
        found = False
        with open("doctor_schedule.txt", 'r') as file:     # Search for the day and update availability
            for line in file:
                data = line.strip().split(" | ")
                if data[0] == day.capitalize():
                    found = True
                    updated_day = day
                    availability = input("Change the availability of this day: ")
                    updated_lines.append(f"{updated_day} | {availability}\n")
                else:
                    updated_lines.append(line)
        if found:
            with open("doctor_schedule.txt", "w") as file:      # Write updated availability back to file
                file.writelines(updated_lines)
            print("Doctor schedule updated.\n")
            input("Press Enter to continue...")
            print("\n" * 20)
        else:
            print("Day not found.Please try again")      # Error if specific day not found
    except Exception as e:
        print(f"Error updating details: {e}")            # Error updating availability


