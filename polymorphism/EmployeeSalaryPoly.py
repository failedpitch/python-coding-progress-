# A company uses different types of employees: FullTimeEmployee, PartTimeEmployee, 
# and ContractEmployee. Each type of employee has a different way of calculating their salary.

# Tasks:

# (a) [2 marks] Define a base class Employee with a method calculate_salary().

# (b) [4 marks] Implement the following subclasses:

# FullTimeEmployee → Salary = basic + 1000 bonus

# PartTimeEmployee → Salary = hours_worked * 50

# ContractEmployee → Salary = contract_amount

# Each subclass should override the calculate_salary() method.

# (c) [2 marks] Write a function pay_employee(employee) that takes an employee object and prints 
# their salary using polymorphism.

# (d) [2 marks] Create one object of each subclass, and call pay_employee() for each.

class Employee:
    def calculate_salary(self):
        return "Uncalculated Without Employee Type."
    
class FullTimeEmployee(Employee):
    def __init__(self):
        self.fte = "Salary = basic + 1000 bonus"
        
    def Employee(self):
        return self.fte
        
class PartTimeEmployee(Employee):
    def __init__(self):
        self.pte = "Salary = hours_worked * 50"
        
    def Employee(self):
        return self.pte
        
class ContractEmployee(Employee):
    def __init__(self):
        self.ce = "Salary = contract_amount"
        
    def Employee(self):
        return self.ce
    
EmployeeTypes = [FullTimeEmployee(), PartTimeEmployee(), ContractEmployee()]

for emp in EmployeeTypes:
    print(emp.Employee())  

    def pay_employee(employee):
        emp=input("Input Employee Type, FullTimeEmployee, PartTimeEmployee, ContractEmployee.")
    
        Salary = 0
        bonus = 1000
    
        if emp == FullTimeEmployee:
            basic = (int(input("Input your basic salary amount.")))
            print ("Your salary is:", Salary = Salary+basic+bonus)
        
        elif emp == PartTimeEmployee:
            hours_worked = (int(input("Input the amount of hours you've worked.")))
            print("Your salary is:", Salary = Salary+hours_worked * 50)
        
        else:
            contract_amount = (int(input("Input your contract salary amount.")))
            print("Your salary is:", Salary+contract_amount)
        
    employee = [FullTimeEmployee, PartTimeEmployee, ContractEmployee]
       
 