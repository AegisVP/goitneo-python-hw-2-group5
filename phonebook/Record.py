from exceptions.Exceptions import DuplicateEntry, PhoneNotFound
from utils.InputError import input_error
from phonebook.Name import Name
from phonebook.Phone import Phone


class Record:
    def __init__(self, name):
        self.name = str(Name(name))
        self.phones = list()
    # end def

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(self.phones)}"
    # end def

    @input_error
    def add_phone(self, phone):
        if phone in self.phones:
            raise DuplicateEntry('Телефон')
        # end if

        self.phones.append(str(Phone(phone)))
        return "Phone number added"
    # end def

    @input_error
    def delete_phone(self, phone):
        phone = str(Phone(phone))

        try:
            self.phones.remove(phone)
        except ValueError:
            raise PhoneNotFound
        # end try

        return "Phone number removed"
    # end def

    @input_error
    def modify_phone(self, old_phone, new_phone):
        try:
            self.phones[self.phones.index(old_phone)] = str(Phone(new_phone))
        except ValueError:
            raise PhoneNotFound
        # end try

        return "Phone number changed"
    # end def

    @input_error
    def find(self, needle):
        if needle not in self.phones:
            raise PhoneNotFound
        return needle
    # end def
