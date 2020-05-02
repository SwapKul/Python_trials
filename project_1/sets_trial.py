#Sets don't follow respective order and can be edited
friends_1 = {"Rolf", "Anne", "Bob"}
friends_2 = {"Rolf", "Joey", "Ted"}

print(friends_1)
print(friends_2)

friends_1.add("Martha")
friends_1.remove("Bob")

print(friends_1)
print(friends_2)

print(friends_1.difference(friends_2))
print(friends_2.difference(friends_1))
print(friends_1.intersection(friends_2))
print(friends_1.union(friends_2))
print(friends_1.symmetric_difference(friends_2))


#Sets comprehension
friends = ["Rolf", "Anne", "Bob", "Joey", "Ted"]
guests = ["Rolf", "Anne", "York", "Joey", "Timmy"]

friends_lower = {f.lower() for f in friends}
guests_lower = {f.lower() for f in guests}

present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
print(present_friends)
#or
present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}
print(present_friends)