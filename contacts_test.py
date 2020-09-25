class Contact(object):
    name = None
    number = None

    def name(self):
        self.name = input("Как вас зовут?: ")

    def number(self):
        self.number = input("Какой у вас номер телефона?: ")


class Contact_book():
    contacts = list()

    def add(self,contact):
        self.contacts.append(contact)

    def print_contacts(self):
        print("Your book:")
        for contact in self.contacts:
            print("--------")
            print(contact.name)
            print(contact.number)
    def search_by_number(self, user_number):
        for contact in self.contacts:
            if contact.number == user_number:
                print(contact.name)
                return
        print("Not found")


if __name__ == '__main__':
    book = Contact_book()

    contact1 = Contact()
    contact1.name()
    contact1.number()

    book.add(contact1)

    contact2 = Contact()
    contact2.name()
    contact2.number()

    book.add(contact2)

    book.print_contacts()

    search_number = input("number: ")
    book.search_by_number(search_number)
