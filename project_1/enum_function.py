friends = ["Rolf", "John", "Anna"]

counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

#OR

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)

for counter, friend in enumerate(friends, start = 1):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))



movies = [("Memento, Christopher Nolan, 2000")]
m_name = input("Please enter a movie title:  ")
m_direc = input("Please enter the director's name:  ")
m_year = input("Please enter the year it released:  ")
new_movie = m_name, m_direc, m_year

print(f"{new_movie[0]}, {new_movie[2]}")

movies.append(new_movie)

print(movies)

