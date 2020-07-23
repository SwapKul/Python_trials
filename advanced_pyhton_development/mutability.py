friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}  # Id changed as we created a new object

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0  # Id won't change as we simply modified the data within the object

print(id(friends_last_seen))

my_int = 5

print(id(my_int))  # Integers, floats and tuples are immutable

my_int = my_int + 1

print(id(my_int))

friends = ['Rolf', 'Jen']

print(id(friends))

friends.append('Jose')

print(id(friends))