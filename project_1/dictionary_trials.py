friends_ages = {"Rolf" : 25, "Anne" : 28, "Bob": 30}

print(friends_ages["Rolf"])
print(friends_ages["Anne"])
print(friends_ages["Bob"])

friends_ages["Bob"] = 21
print(friends_ages)

friends = [
    {"name" : "Rolf Smith", "age" : 24},
    {"name" : "Adam Wool", "age" : 30},
    {"name" : "Anne Pun", "age" : 27}
]

print(friends[0]["name"])
print(friends[1]["age"])

#Dictionary comprehensions
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}

print(long_timers)
#or
dictionary = dict(zip(friends, time_since_seen))
print(dictionary)
dictionary = list(zip(friends, time_since_seen, [1, 2, 3, 4, 5]))
print(dictionary)