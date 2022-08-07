import copy

class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'

# address = Address('123 Main Street', 'Anytown', 'USA')
# john = Person('John', address)
# print(john)

# jane = Person('Jane', address)
# jane.name = 'Jane'
# print('------------------')
# jane.address.street_address = '123b London Road'
# print(john)
# print(jane)


john = Person('John', Address('123 Main Street', 'Anytown', 'USA'))
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = '123b London Road'
print(john)
print(jane)