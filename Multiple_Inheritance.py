class employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def display(self):
        print(self.name)
        print(self.emp_id)

class wageMixin:
    def __init__(self, hours_worked, hours_rate):
        self.hw = hours_worked
        self.hr = hours_rate
    def calculate_pay(self):
        return self.hw * self.hr

class salaryMixin:
    def __init__(self, annual_pay):
        self.a = annual_pay
    def calculate_pay(self):
        return self.a / 12

class salary_emp(employee, salaryMixin):
    def __init__(self, name, emp_id, annual_pay):
        employee.__init__(self, name, emp_id)
        salaryMixin.__init__(self, annual_pay)
    def display_info(self):
        super().display()
        print(f"Salary : ${self.calculate_pay()} per month")

class wage_emp(employee, wageMixin):
    def __init__(self, name, emp_id, hours_worked, hours_rate):
        employee.__init__(self, name, emp_id)
        wageMixin.__init__(self, hours_worked, hours_rate)
    def display_info(self):
        super().display()
        print(f"Wage : ${self.calculate_pay()} per month")

wage_employee = wage_emp("John", 1001, 40, 100)
wage_employee.display_info()
salary_employee = salary_emp("Jane", 1002, 500000)
salary_employee.display_info()
