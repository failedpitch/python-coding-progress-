class Employee:
    def calculate_salary(self):
        return "Uncalculated Without Employee Type."


class FullTimeEmployee(Employee):
    def __init__(self, basic):
        self.basic = basic

    def calculate_salary(self):
        return self.basic + 1000


class PartTimeEmployee(Employee):
    def __init__(self, hours_worked):
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hours_worked * 50


class ContractEmployee(Employee):
    def __init__(self, contract_amount):
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount


def pay_employee():
    choice = input("Enter employee type (FullTime/PartTime/Contract): ")
    if choice.lower() == "fulltime":
        basic = int(input("Enter basic salary: "))
        emp = FullTimeEmployee(basic)
    elif choice.lower() == "parttime":
        hours = int(input("Enter hours worked: "))
        emp = PartTimeEmployee(hours)
    elif choice.lower() == "contract":
        amount = int(input("Enter contract amount: "))
        emp = ContractEmployee(amount)
    else:
        print("Invalid choice")
        return
    print("Salary:", emp.calculate_salary())


pay_employee()