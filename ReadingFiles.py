
employee_file = open("employees", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()