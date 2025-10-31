from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)

        # Validate that provided number is in format of 10 numbers
        for char in value:
            if not char.isdigit():
                raise ValueError("Phone number must contain only digits")

        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        if phone not in self.phones:
            new_phone = Phone(phone)
            self.phones.append(new_phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            index = self.phones.index(phone)
            self.phones[index] = Phone(new_phone)

    def find_phone(self, name):
        for phone in self.phones:
            if phone == name:
                return phone

        return None

    def __str__(self):
        return (f"Contact name: {self.name.value}, "
                f"phones: {'; '.join(p.value for p in self.phones)}")


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Name not found, please try again.")

    return inner


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    @input_error
    def add_record(self, record: Record):
        self.data.update({record.name.value: record})
        print(f"Added {record.name}")

    @input_error
    def find(self, name: str) -> Record | None:
        return self.data[name]

    @input_error
    def delete(self, name):
        target_record = self.find(name)
        if target_record is not None:
            self.data.pop(target_record)
            print(f"Contact {name} deleted")
