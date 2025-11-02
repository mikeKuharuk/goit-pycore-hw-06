from address_book import AddressBook, Record

print("Welcome to Address Book")
# Creating new address book
book = AddressBook()

# Creating John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# Trying to add duplicate
john_record.add_phone("5555555555")

# Adding John to book
book.add_record(john_record)

# Creating and adding Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all entries in book
for name, record in book.data.items():
    print(record)

# Find and edit number in book
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Print: Contact name: John, phones: 1112223333; 5555555555

# Search for specific phone number John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Print: 5555555555

# Removing Jane from book
book.delete("Jane")
