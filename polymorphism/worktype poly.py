class Work:
    def work(self):
        return "Generic work"

class Manager(Work):
    def __init__(self):
        self.manager_work = "Manage things or something"

    def work(self):
        return self.manager_work

class Developer(Work):
    def __init__(self):
        self.developer_work = "Make a development"

    def work(self):
        return self.developer_work

class Intern(Work):
    def __init__(self):
        self.intern_work = "Unpaid intern, get me a coffee"

    def work(self):
        return self.intern_work

employees = [Manager(), Developer(), Intern()]

for emp in employees:
    print(emp.work())