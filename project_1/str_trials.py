name = input("Please enter your name:  ")
age = int(input("Please enter your age:  "))

# using int above helps python to figure that age has integer value
print(f"{name} is {age} years old i.e {age * 12} months and {age * 365} days".capitalize())