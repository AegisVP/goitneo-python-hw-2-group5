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
            print("Недостатнь данних введено")
            raise
        except NoPhoneEntered:
            print("Введіть номер телефона")
            raise
        except PhoneNotFound:
            print("Номер телефона не знайдено")
            raise
        except IncorrectPhoneFormat:
            print("Введіть 10 цифр як номер телефона")
            raise
        except NoDataFound:
            print("Нічого не знайдень")
            raise
        except IncorrectDataType:
            print("Некорректний тип данних")
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
