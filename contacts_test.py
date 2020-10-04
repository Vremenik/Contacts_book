class Contact(object):
    name = None
    number = None


    def name(self):
        self.name = input("Как вас зовут?: ")

    def number(self):
        self.number = input("Какой у вас номер телефона?: ")

    def change_number(self, new_number):
        self.number = new_number





class Contact_book():
    contacts = []

    def list(self):
        print("Your book:")
        for contact in self.contacts:
            print("--------")
            print(contact.name)
            print(contact.number)

    def find_by_number(self):
        user_number = input("Введите номер пользователя: ")
        for contact in self.contacts:
            if contact.number == user_number:
                print(contact.name)
                return contact
        print("Not found")

        print("Контакт не найден")

    def find_by_name(self):
        user_name = input("Введите имя пользователя: ")
        for contact in self.contacts:
            if contact.name == user_name:
                print(contact.number)
                return contact
        print("Not found")

        print("Контакт не найден")

    def add_new(self):
        new_contact = Contact()
        new_contact.name()
        new_contact.number()
        self.contacts.append(new_contact)

    def add(self, new_contact):
        self.contacts.append(new_contact)

    def delete(self):
        print("Введите имя контакт: ")
        name = input('> ')
        for contact in self.contacts:
            if contact.name == name:
                print("Вы хотите удалить контакт %s (yes/no)?: " % name)
                name_del = input('> ')
                if name_del == 'yes':
                    self.contacts.remove(contact)
                    print("Вы удалили контакт %s " % name)

    def edit(self):
        print("Введите имя контакта: ")
        name = input('> ')
        for contact in self.contacts:
            if contact.name == name:
                new_number = input("Введите новый номер: ")
                contact.change_number(new_number)






if __name__ == '__main__':

    contact1 = Contact()
    contact1.name()
    contact1.number()

    contact2 = Contact()
    contact2.name()
    contact2.number()

    my_book = Contact_book()
    my_book.add(contact1)
    my_book.add(contact2)

    print("Добро пожаловать в телефонную книгу.")
    print("""Введите команду:
    * list - чтобы посмотреть список контактов.
    * findn- найти контакт по имени
    * findm - найти контакт по номеру
    * add  - добавить контакт
    * del  - удаление контакта
    * edit - изменение контакта
    * exit - выход""")

    while True:
        print("\nВведите команду: ")
        command = input('> ')
        if command == 'list':
            my_book.list()
        elif command == 'findm':
            my_book.find_by_number()
        elif command == 'findn':
            my_book.find_by_name()
        elif command == 'add':
            my_book.add_new()
        elif command == 'del':
            my_book.delete()
        elif command == 'edit':
            my_book.edit()
        elif command == 'exit':
            break
        else:
            print("Неизвестная команда")