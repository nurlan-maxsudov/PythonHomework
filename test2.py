import pandas as pd

department_data = [
    {"DeptID": 1, "DeptName": "Finance"},
    {"DeptID": 2, "DeptName": "IT"},
    {"DeptID": 3, "DeptName": "HR"}
]

# Employee data as a list of dictionaries
employee_data = [
    {"EmpID": 101, "EmpName": "Isha", "DeptID": 1, "EmpSalary": 7000},
    {"EmpID": 111, "EmpName": "Esha", "DeptID": 1, "EmpSalary": 8970},
    {"EmpID": 102, "EmpName": "Mayank", "DeptID": 1, "EmpSalary": 8900},
    {"EmpID": 103, "EmpName": "Ramesh", "DeptID": 2, "EmpSalary": 4000},
    {"EmpID": 104, "EmpName": "Avtaar", "DeptID": 2, "EmpSalary": 9000},
    {"EmpID": 105, "EmpName": "Gopal", "DeptID": 3, "EmpSalary": 17000},
    {"EmpID": 106, "EmpName": "Krishna", "DeptID": 3, "EmpSalary": 1000},
    {"EmpID": 107, "EmpName": "Suchita", "DeptID": 3, "EmpSalary": 7000},
    {"EmpID": 108, "EmpName": "Ranjan", "DeptID": 3, "EmpSalary": 17900}
]

df_department = pd.DataFrame(department_data)
df_employee = pd.DataFrame(employee_data)

# print(df_department)
# print(df_employee)

df_highest = df_employee.sort_values(by="EmpSalary", ascending=False)
df_highest = df_highest.groupby("DeptID")["EmpSalary"].nth(1)

merged_df = pd.merge(df_highest, df_employee, on="EmpSalary", how="inner")
print(merged_df)

result_df = pd.merge(merged_df, df_department, on="DeptID")
print(result_df)

print(result_df[["EmpID", "EmpName", "EmpSalary", "DeptName"]])
