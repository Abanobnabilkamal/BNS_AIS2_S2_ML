
def view_staff_info(department):
    name = input("Enter staff name: ")

    for staff_member in department.staff:
        if staff_member.name == name:
            print(staff_member.view_info())
            return

    print("Staff member not found.")