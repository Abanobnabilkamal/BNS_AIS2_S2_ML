from project import Patient

def add_patient(department):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    medical_record = input("Enter medical record: ")

    patient = Patient(name, age, medical_record)

    department.add_patient(patient)