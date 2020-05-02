movie_list = []

def add_movie():
    title = input("Please enter the movie title:  ")
    director = input("Please enter the director's name:  ")
    year = input("Please enter the year it got released:  ")

    movie_list.append({
        "title" : title,
        "director" : director,
        "year" : year
    })

add_movie()
