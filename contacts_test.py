class Contact(object):
    name = None
    number = None

    def name(self):
        self.name = input("Как вас зовут?: ")

    def number(self):
        self.number = input("Какой у вас номер телефона?: ")

class Contact_book():
    contacts = []

    def list(self):
        print("Your book:")
        for contact in contacts:
            print("--------")
            print(contact.name)
            print(contact.number)

    def find(self, user_number):
        for contact in self.contacts:
            if contact.number == user_number:
                print(contact.name)
                return
        print("Not found")

        print("Контакт не найден")


    def add(self, contact):
        self.contacts.append(contact)

contact1 = Contact()
contact1.name()
contact1.number()

contact2 = Contact()
contact2.name()
contact2.number()




print("Добро пожаловать в телефонную книгу.")
print("""Введите команду:
* list - чтобы посмотреть список контактов.
* find - найти контакт по имени
* add  - добавить контакт
* del  - удаление контакта
* edit - изменение контакта
* exit - выход""")

while True:
    print("\nВведите команду: ")
    command = input('> ')
    if command == 'list':
        list()
    elif command == 'find':
        find()
    elif command == 'add':
        add()
    elif command == 'del':
        delete()
    elif command == 'edit':
        edit()
    elif command == 'exit':
        break
    else:
        print("Неизвестная команда")


