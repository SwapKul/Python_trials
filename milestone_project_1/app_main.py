prompt = ("\nPlease enter: 'a' to add a movie; 'l' to see your movie list; 'f' to find a movie by its title or 'q' to exit: ")
movie_list = []


def add_movie():
    title = input("Please enter the movie title:  ")
    director = input("Please enter the director's name:  ")
    year = input("Please enter the year it got released:  ")

    movie_list.append({
        "title": title,
        "director": director,
        "year": year
    })


def show_movies():
    for movie in movie_list:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")


def find_movie():
    search_title = input("Please enter the title of the movie you're looking for:  ")

    for movie in movie_list:
        if movie["title"] == search_title:
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}


def menu():
    selection = input(prompt)
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please try again.")

        selection = input(prompt)


menu()
