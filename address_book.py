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

        if not value.isdigit():
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

    def find_phone(self, target_phone):
        for phone in self.phones:
            if phone.__str__() == target_phone:
                return phone

        return None

    def __str__(self):
        return (f"Contact name: {self.name.value}, "
                f"phones: {'; '.join(p.value for p in self.phones)}")


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def find(self, name: str) -> Record | None:
        return self.get(name, None)

    def delete(self, name):
        target_record = self.find(name)
        if target_record is not None:
            self.data.pop(name)
