open("employees.txt", "a") #append
open("employees.txt", "r") #read
open("employees.txt", "w") #write
open("employees.txt", "r+") #read and write
employee_file = open("employees.txt", "r+") #variable
for employee in employee_file.readlines():
    print(employee)
employee_file.close()#always close a file
