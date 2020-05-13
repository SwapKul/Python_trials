def hunred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hunred_numbers()
print(g)
print(next(g))
print(next(g))
print(next(g))
print("Hello")
print(next(g))