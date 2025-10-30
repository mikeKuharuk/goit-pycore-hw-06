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

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)
            print(f"Added {phone} to {self.name}")
        else:
            print(f"Already added to {self.name}")

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
            print(f"Removed {phone} from {self.name}")
        else:
            print(f"Phone {phone} is not in {self.name}")

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            index = self.phones.index(phone)
            self.phones[index] = new_phone
            print(f"Updated {phone} to {self.name}")
        else:
            print(f"Phone {phone} is not in {self.name}")

    def find_phone(self, name):
        for phone in self.phones:
            if phone == name:
                return phone

        print(f"Contact {name} not found")
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data.update({record.name: record})
        print(f"Added {record.name}")

    def find(self, name: str) -> Record | None:
        for record in self.data.items():
            if record[0].value == name:
                return record[1]

        print(f"Contact {name} not found")
        return None

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            print(f"Contact {name} deleted")
        else:
            print(f"Contact {name} not found")
