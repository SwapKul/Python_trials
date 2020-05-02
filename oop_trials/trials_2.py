class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def __repr__(self):
        return f"This is {self.name}'s info"

    @property
    def pay_grade(self):
        if self.salary > 500000:
            return (f"{self.name} has a High pay grade.")
        else:
            return (f"{self.name} has a Low pay grade.")


Employee_1 = Employee("Mafee", "I.T.", 650000)
Employee_2 = Employee("Taylor", "Logistics", 750000)
Employee_3 = Employee("Ben", "Analysis", 450000)

print(Employee_1.pay_grade)
print(Employee_3.pay_grade)
print(Employee_2.department)
print(Employee_1)