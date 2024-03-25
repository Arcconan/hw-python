from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value


class Name(Field):

    def __init__(self, value):
        super().__init__(value)


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        self.phone_valid()

    def phone_valid(self):
        if self.value is not None:
            if len(self.value) != 10 or not self.value.isdigit():
                raise ValueError("Your phone must contain 10 digit")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_number = Phone(phone)
        phone_number.phone_valid()
        self.phones.append(phone_number)

    def remove_phone(self, phone):
        for element in self.phones:
            if element.value == phone:
                self.phones.remove(element)

    def edit_phone(self, phone, new_phone):
        for element in self.phones:
            if element.value == phone:
                element.value = new_phone
                return
        raise ValueError(f'Phone {phone} not found')

    def find_phone(self, phone):
        for element in self.phones:
            if element.value == phone:
                return element

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    book = AddressBook()