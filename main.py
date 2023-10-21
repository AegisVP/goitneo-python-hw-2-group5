from variables import help_text
from phonebook.Record import Record
from phonebook.AddressBook import AddressBook
from utils.InputError import input_error
from exceptions.Exceptions import NoPhoneEntered, UserNotFound
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


book = AddressBook()


def find_records(*data):
    found = []
    for needle in data:
        res = book.find(needle)
        if res:
            found.append(res)
        # end if
    # end for

    return print_data(found) if len(found) > 0 else "Nothing found"
    # end for
# end def


def find_record(needle):
    record = book.find(needle)

    if record == None:
        raise UserNotFound
    # end if

    return record
# end def


def add_entry(name, *phones):
    new_record = book.find(name) or Record(name)

    for phone in phones:
        new_record.add_phone(phone)
    # end for

    return book.add_record(new_record)
# end def


def delete_entry(name, phone=None):
    if phone == None:
        return book.delete_record(name)
    # end if
    return delete_phone(name, phone)
# end def


def modify_phone(name, old_phone, new_phone):
    record = find_record(name)

    record.modify_phone(old_phone, new_phone)
    return book.modify_record(record)
# end def


def delete_phone(name, phone):
    record = find_record(name)
    record.delete_phone(phone)
    return book.modify_record(record)
# end def


def print_data(data=[]):
    if len(book) > 0:
        return "\n".join([str(record) for record in data])
    # end if
    return "Phonebook is empty"
# end def


def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
        # end try
    # end def
    return wrapper


@try_catch_wrapper
def run_bot():
    global book
    print("Welcome! What can I do for you?")

    while True:
        try:
            user_input = input(">>> ")
            if len(user_input) == 0:
                continue
            # end if

            command, *data = user_input.strip().split()
            command = command.casefold()

            if command in ["hello", "hi"]:
                print("How can I help you?")
            elif command in ["add", "new", "add_phone", "new_phone"]:
                print(add_entry(*data))
            elif command in ["delete", "remove", "delete_phone", "remove_phone"]:
                print(delete_entry(*data))
            elif command in ["edit", "change", "modify"]:
                pass
            elif command in ["show", "find"]:
                print(find_records(*data))
            elif command in ["all", "list", "list-all"]:
                print(print_data(book.return_phonebook()))
            elif command in ["help"]:
                print(help_text)
            elif command in ['close', 'quit', 'exit', 'bye']:
                print("Good bye!")
                break
            else:
                print("Try asking something else or type 'help'")
            # end if
        except Exception:
            continue
        # end try
    # end while
# end def


if __name__ == "__main__":
    run_bot()
# end if
