name = input("Please enter employee's name:  ").title().strip()
hourly_wage = int(input("Please enter your hourly wage:  "))
hours_worked = int(input("Please enter the number of hours worked in this week:  "))
print(f"{name} earned Rs.{hourly_wage * hours_worked} this week.")