from project import Staff


def add_staff(department):
    name = input("Enter staff name: ")
    age = int(input("Enter staff age: "))
    position = input("Enter staff position: ")

    staff_member = Staff(name, age, position)

    department.add_staff(staff_member)