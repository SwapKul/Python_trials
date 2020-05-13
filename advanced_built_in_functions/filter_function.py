def starts_with_r(friend):
    return friend.startswith('R')


friends = ['Rolf', 'Anna', 'Jose', 'Randy', 'Mary', 'Rose']
start_with_r = filter(starts_with_r, friends)

print(next(start_with_r))
print(next(start_with_r))
print(next(start_with_r))
print(list(start_with_r))
print(list(start_with_r))
print(list(start_with_r))

# or

friendss = ['Rolf', 'Anna', 'Jose', 'Randy', 'Mary', 'Rose']
startwith_r = filter(lambda friend: friend.startswith('R'), friendss)

print(next(startwith_r))
print(next(startwith_r))
print(next(startwith_r))

# or

frands = ['Rolf', 'Anna', 'Jose', 'Randy', 'Mary', 'Rose']
another_starts_with_R = (f for f in frands if f.startswith('R'))

print(next(another_starts_with_R))

# or

def my_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i