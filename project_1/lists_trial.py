#Lists follow respective order and can be edited i.e they are mutable
friends = ["Rolf", "Anne", "Bob"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends)
friends.append("joey")
print(friends)
friends[0] = "John"
print(friends)
friends.remove("John")
print(friends)
print(", ".join(friends))

friends_info = [["Ted", 24], ["Marshall", 28], ["Barney", 27]]
print(friends_info[0][1])

#List slicing
friends = ["Rolf", "Anne", "Bob", "Joey", "Ted"]
print(friends[2:4])
print(friends[1:])
print(friends[:4])
print(friends[-3:])
print(friends[-3:4])
print(friends[:-3])
print(friends[2:-2])
print(friends[:])


#list comprehension
numbers = [0, 1, 2, 3, 4, 5]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

double_numbers = [number * 2 for number in numbers]
print(double_numbers)
#or
d_numbers = [number * 2 for number in range(6)]
print(d_numbers)

friends_name = [f"{name} is my friend." for name in friends]
print(friends_name)
print(', '.join(friends_name))
friends_lower = [name.lower() for name in friends_name]
print(friends_lower)


#list comprehension with conditionals
ages = [22, 34, 45, 31, 56, 75]
odds = [age for age in ages if age % 2 == 1]
print(odds)

#w/o comprehension
friends = ["Rolf", "Anne", "Bob", "Joey", "Ted"]
guests = ["Rolf", "Anne", "York", "Joey", "Timmy"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))

#with comprehension
friends = ["Rolf", "Anne", "Bob", "Joey", "Ted"]
guests = ["Rolf", "Anne", "York", "Joey", "Timmy"]

friends_lower = [f.lower() for f in friends]
present_friends = [
    name for name in guests if name.lower() in friends_lower
]
print(present_friends)

numbers = [1, 2, 4, 5]
numbers.insert(2, 3)
print(numbers)
del numbers[0]
print(numbers)
#or
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
numbers.clear()
print(numbers)
numbers.extend('1')
print(numbers)

#using split call
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_list = user_numbers.split(",")

print(numbers_list) # ['1', '2', '3', '4', '5']

#or
user_numbers = input("Please enter 5 numbers separated by dashes: ") # 1-2-3-4-5
numbers_tuple = user_numbers.split("-")

print(numbers_tuple) # ['1', '2', '3', '4', '5']

#or
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_tuple = tuple(user_numbers.split(","))

print(numbers_tuple) # ('1', '2', '3', '4', '5')

#converting strings into lists/ tuples
print("That must have felt quite good\nbut still not as much as i thought")

friends_name = input("Please enter name of any 5 friends of yours separated by commas:  ")
friends_name = friends_name.split(",")

final_list = []

for name in friends_name:
    final_list.append(name.title().strip())

print(final_list)

age = "Exaggerate"
print(list(age))
print(tuple(age))

question = ["5and6", "6and5", "8and8"]
for x in question:
    i, f = x.split("and")
    print(f"{i} is initial and {f} is final")