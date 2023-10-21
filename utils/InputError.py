from exceptions.Exceptions import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Значення не правильне")
            raise
        except KeyError:
            print("Значення не знайдене")
            raise
        except IndexError as e:
            print(e)
            raise
        except NoDataEntered:
            print("Not enough data entered")
            raise
        except NoPhoneEntered:
            print("Enter a phone number")
            raise
        except PhoneNotFound:
            print("Phone number not found")
            raise
        except IncorrectPhoneFormat:
            print("Enter only 10 digits as phone number")
            raise
        except NoDataFound:
            print("Nothing found")
            raise
        except IncorrectDataType:
            print("Wrong data type passed")
            raise
        except DuplicateEntry as e:
            entry_msg = e if e.args.__len__ else 'Запис'
            print(f"{entry_msg} вже існує")
            if entry_msg == "Контакт":
                print("Use add_phone to add additional phone numbers")
            raise

        except Exception as e:
            print(e)
            raise
        # end try
    return inner
# end def
