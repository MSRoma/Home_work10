from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value  


class Name(Field):
    pass


class Phone(Field):
    pass  


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name 
        self.phones = []
        if phone: 
            self.phones.append(phone)
    
    def add_phone(self, phone: str):
        phone_number = Phone(phone) 
        self.phones.append(phone_number)

    def delete_phone(self, phone: str):
        for ph_obj in self.phones:
            if ph_obj.value == phone:
                self.phones.remove(ph_obj)

    def edit_phone(self, old_phone: str, new_phone: str):
        for ph_obj in self.phones:
            if ph_obj.value == old_phone:
                index = self.phones.index(old_phone)
                self.phones[index] = new_phone

class AddressBook(UserDict):
    def add_record(self, rec):
        self.data[rec.name.value] = rec



if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')