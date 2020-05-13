from utils import database

USER_CHOICE = """
Enter your choice:
- 'a' to add an entry
- 'f' to find an entry
- 'l' to list an entry
- 'd' to delete an entry
- 'q' to quit
Enter your choice:  """


def menu():
    database.create_entry_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_entry()
        elif user_input == 'f':
            prompt_find_entry()
        elif user_input == 'l':
            list_entries()
        elif user_input == 'd':
            prompt_delete_entry()
        else:
            print('Unknown command. Please try again!!')

        user_input = input(USER_CHOICE)


def prompt_add_entry():
    customer_id = input("Please enter the customer ID:  ")
    customer_name = input("Please enter customer's name:  ")
    bill_amt = input("Please enter billing amount:  ")

    database.add_entry(customer_id, customer_name, bill_amt)


def prompt_find_entry():
    customer_name = input("Please enter customer's name:  ")

    database.find_entry(customer_name)


def list_entries():
    database.show_entries()


def prompt_delete_entry():
    customer_id = input("Please enter customer ID:  ")

    database.delete_entry(customer_id)


menu()
