filename = "C:\\Users\\ids\\Desktop\\PythonHomework\\lesson-6\\homework\\employees.txt"


def add_employee(filename = "C:\\Users\\ids\\Desktop\\PythonHomework\\lesson-6\\homework\\employees.txt"):

    employee_id = input("Enter employee ID: ").strip()
    name = input("Enter employee name: ").strip()
    position = input("Enter employee position: ").strip()
    salary = input("Enter employee salary: ").strip()

    employee = f"{employee_id}, {name}, {position}, {salary}"

    try:
        with open(filename, "a") as file:
            file.write(employee + "\n")
        print("Employee record added successfully!")

    except Exception as e:
        print("Error: ", e)

def view_records(filename = "C:\\Users\\ids\\Desktop\\PythonHomework\\lesson-6\\homework\\employees.txt"):
    try:
        with open(filename, mode="r") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print("Error: ", e)

filename = "C:\\Users\\ids\\Desktop\\PythonHomework\\lesson-6\\homework\\employees.txt"

def search_employee(filename = "C:\\Users\\ids\\Desktop\\PythonHomework\\lesson-6\\homework\\employees.txt"):

    employee_data = []
    
    ID = input("Enter ID of employee: ")

    try:
        with open(filename, "r") as file:
            for line in file:
                employee = line.split(",")
                employee_data.append(employee)
            
        is_found = False
        index = 0
        for i in range(len(employee_data)):
            if ID == int(employee_data[i][0]):
                is_found = True
                index = i
        
        if is_found:
            for j in range(4):
                print(employee_data[index][j], end="")
    except Exception as e:
        print(f"Error: {e}")

def update_employee(filename = "C:\\Users\\ids\\Desktop\\PythonHomework\\lesson-6\\homework\\employees.txt"
):
    ID = input("Enter Employee ID to update: ").strip()
    updated = False
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        with open(filename, "w") as file:
            for line in lines:
                if line.strip().startswith(ID + ","):
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    file.write(f"{ID}, {name}, {position}, {salary}\n")
                    updated = True
                else:
                    file.write(line)
        if updated:
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")


# ID = input("Enter employee ID: ")
# update_employe_info(ID)

def delete_employee(filename = "C:\\Users\\ids\\Desktop\\PythonHomework\\lesson-6\\homework\\employees.txt"):
    ID = input("Enter Employee ID to delete: ")
    deleted = False
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        with open(filename, "w") as file:
            for line in lines:
                if not line.startswith(ID + ","):
                    file.write(line)
                else:
                    deleted = True
        if deleted:
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")



print("Please, choose one of the options: ")
menu = "\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by employee ID"
menu += "\n4. Update employee's information\n5. Delete en employee record\n6. Exit\n"


is_on = True

while(is_on):
    answer = input(menu).strip()
    if answer == "1":
        add_employee()
    elif answer == "2":
        view_records()
    elif answer == "3":
        search_employee()
    elif answer == "4":
        update_employee()
    elif answer == "5":
        delete_employee()
    elif answer == "6":
        is_on = False
    
    