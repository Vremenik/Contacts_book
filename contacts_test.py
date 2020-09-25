contacts = list()

class Contact(object):
    name = None
    number = None

    def name(self):
        self.name = input("Как вас зовут?: ")

    def number(self):
        self.number = input("Какой у вас номер телефона?: ")

contact1 = Contact()
contact1.name()
contact1.number()

contact2 = Contact()
contact2.name()
contact2.number()

contacts.append(contact1)
contacts.append(contact2)

print("Данные сохранены")

while True:
    a = input("Введите ваше имя: ")
    if a == contact1.name:
        print("Ваш номер: " + str(contact1.number))

    if a == contact2.name:
            print("Ваш номер: " + str(contact2.number))

    if a == str(0):
        break

    if not a == contact1.name and not a == contact2.name and not a == str(0):
        print("Такого имени нет в базе данных")

    
