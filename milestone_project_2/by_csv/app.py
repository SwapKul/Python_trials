from by_csv.utils import database

USER_CHOICE = """
ENTER:
- 'a' to add a book
- 'l' to list all books
- 'f' to find a book
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit the program

Your Choice:  """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'f':
            prompt_find_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown Command. Please try again.")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Please enter the name of the book:  ")
    author = input("Please enter the name of the author:  ")

    database.add_book(name, author)


def list_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] == "1" else 'NO'
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_find_book():
    name = input("Please enter the name of the book:  ")

    database.find_book(name)


def prompt_read_book():
    name = input("Please enter the name of the book you read:  ")
    database.mark_as_read(name)


def prompt_delete_book():
    name = input("Please enter the name of the book you want to delete: " )
    database.delete_book(name)


menu()