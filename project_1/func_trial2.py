def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg  # Ends the function, gives back the value


def car_name(car):
    return f"{car['make']} {car['model']}"


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon.")
    # Returns None by default, as all functions do


cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    print_car_info(car)

def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


print(divide(10, 2))
print(divide(6, 0))

# Lambda functions are functions that are almost solely used to get inputs and return outputs.
# That means we don't often use them to make actions.
# For example, the `print()` function is a function that performs an action. As such, it would not be suitable for lambda function.
# If we wanted a function that just divided two numbers, that might be suitable for a lambda function.

# That's because that function takes inputs, processes them, and returns outputs. And, it's a short, simple function. You'll see why that is relevant with this example.

divide = lambda x, y: x / y
# This spacing is common. After each comma in the parameters, after the colon but not before, and between operators (though that's optional, and sometimes will be seen without spaces).

# That is a lambda function, which takes two arguments and returns the result of dividing one by the other. It is almost identical to this function:
print(divide(15, 3))

def divide(x, y):
    return x / y


# In both cases you would call it as a normal function:

print(divide(15, 3))

# While traditional functions _need_ the name (you can't define one without it), lambda functions don't have names unless you assign them to a variable.

result = (lambda x, y: x + y)(15, 3)
print(result)

# However you can see that lambda functions can be quite difficult to read, so we won't be using them very often. The main reason to use lambda function is because they are short, so if we use them in conjunction with other functions that can help make our programs a bit more flexible.

# Here's an example. Instead of this:


def average(sequence):
    return sum(sequence) / len(sequence)


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))

# Since the average function just takes inputs and returns an output, we could re-define it as a lambda function.

average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))
