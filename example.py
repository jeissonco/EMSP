class Person:
    def __init__(self, name):
        self.name =name

    def get_name(self):
        print(f'{self.name}')
    

person1 = Person("Jeisson")

person1.get_name()
