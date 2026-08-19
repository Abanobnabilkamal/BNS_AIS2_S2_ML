
def view_patient_record(department):
    name = input("Enter patient name: ")

    for patient in department.patients:
        if patient.name == name:
            print(patient.view_record())
            return

    print("Patient not found.")
    
