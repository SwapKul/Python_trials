class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


ford = Garage()
ford.cars.append("Fiego")
ford.cars.append("Fiesta")

print(ford.cars)
print(ford[0])

for car in ford:
    print("\n",car)