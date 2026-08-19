
from project import Department

def add_department(hospital):
    
    name = input("Enter department name: ")

    department = Department(name)

    hospital.add_department(department)

    print("Department added successfully.")
    