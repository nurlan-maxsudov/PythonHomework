import os

class Employee:
    
    def __init__(self, id, name, position, salary):
        self.employee_id = id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}"
    
    def from_string(employee_str):
        employee_id, name, position, salary = employee_str.strip().split(",")
        return Employee(employee_id, name, position, float(salary))

class EmployeeManager:
    
    FILE_NAME = "lesson-7\homework\employee.txt"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w") as f:
                pass
    
    def add_employee(self):
        name = input("Name: ")
        id = int(input("ID: "))
        position = input("Position: ")
        salary = input("Salary: ")
        
        employee = Employee(id, name, position, salary)
        with open(self.FILE_NAME, "a") as f:
            f.write(str(employee) + "\n")
            
    def _load_employees(self):
        employees = []
        with open(self.FILE_NAME, "r") as f:
            for line in f:
                if line.strip():
                    employees.append(Employee.from_string(line))
        return employees        
    
    def view_employees(self):
        employees = self._load_employees()
        emp: Employee
        for emp in employees:
            print(f"ID:{emp.employee_id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}")
    
#  Search for an employee by Employee ID

    def search(self, ID):
        employees = self._load_employees()
        emp: Employee
        
        for emp in employees:
            if (emp.employee_id == ID):
                print(f"ID:{emp.employee_id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}")
            else:
                raise ValueError("There is no Employee with such ID")

    def update_employee(self, employee_id, new_name=None, new_position=None, new_salary=None):
        employees = self._load_employees()
        updated = False
        
        for emp in employees:
            if emp.employee_id == employee_id:
                if new_name:
                    emp.name = new_name
                if new_position:
                    emp.position = new_position
                if new_salary is not None:
                    emp.salary = float(new_salary)
                updated = True
                break
        if updated:
            with open(self.FILE_NAME, "w") as f:
                for emp in employees:
                    f.write(str(emp) + "\n")
    def delete_employee(self, id):
        employees = self._load_employees()
        emp: Employee
        
        employees = [emp for emp in employees if emp.employee_id != id]
        
        with open(self.FILE_NAME, "w") as f:
            for emp in employees:
                f.write(str(emp) + "\n")
    
    def exit(self):
        os._exit()

if __name__ == "__main__":
    manager = EmployeeManager()
    emp = Employee("777", "Nurlan", "Data engineer", 75000)

    message = '''Welcome to the Employee Records Manager!
    1. Add new employee record
    2. View all employee records
    3. Search for an employee by Employee ID
    4. Update an employee's information
    5. Delete an employee record
    6. Exit'''

    print(message)

    is_on = True
    
    while(is_on):
        
        res = int(input("Enter your choice: "))
        
        if res == 1:
            manager.add_employee()
        elif res == 2:
            manager.view_employees()
        elif res == 3:
            id = int(input("Employee ID: "))
            manager.search(id)
        elif res == 4:
            id = int(input("Employee ID: "))
            manager.update_employee(id)
        elif res == 5:
            id = int(input("Employee ID: "))
            manager.delete_employee(id)
        elif res == 6:
            manager.exit()
            
