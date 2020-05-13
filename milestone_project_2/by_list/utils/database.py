books =[]

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def show_books():
    for book in books:
        read = ('Yes' if book["read"] == True else 'No')
        print(f'{book["name"]} by {book["author"]}, read: {read}.')


def find_book(name):
    for book in books:
        if book["name"] == name:
            print(f'{book["name"]} by {book["author"]}.')


def mark_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True


def delete_book(name):
    for book in books:
        if book["name"] == name:
            books.remove(book)