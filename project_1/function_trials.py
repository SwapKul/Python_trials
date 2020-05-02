def greet():
    name = input("Please enter your name:  ")
    print(f"Hello! {name.title().strip()}.")

greet()


#the value in the bracket in "Parameter"
def calculate_mpg(car_to_be_calculated):
    mpg = car_to_be_calculated["mileage"] / car_to_be_calculated["fuel_consumed"]
    name = f"{car_to_be_calculated['make']} {car_to_be_calculated['model']}"
    print(f"{name} does {mpg} miles per gallon.")

#the value in the bracket in "Argument"
calculate_mpg({
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fuel_consumed": 460
})

calculate_mpg({
        "make": "Mercedes",
        "model": "Benz",
        "mileage": 15000,
        "fuel_consumed": 500
})

#or
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

def calc_mpg(car, intro):
    print(intro)
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")

calc_mpg(cars[0], "New Car")
calc_mpg(cars[1], "New Car")
calc_mpg(cars[2], "New Car")
#OR
for car in cars:
    calc_mpg(car, "New Car")