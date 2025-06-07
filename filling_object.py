import csv

class Persona:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    #printing function of the object
    def __str__(self):
        return f"{self.name}, {self.age} años, vive en {self.city}"
    
    def to_dict(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "City": self.city
        }


def input_person():
    name = input('enter a name: ')

    while True:
        try:
            age = int(input('Enter age: '))
            break
        except ValueError:
            print("Invalid age. Enter an enter number")

    city = input('enter a city: ')

    return Persona(name, age, city)

people = []


people.append(input_person())


"""

for p in people:
    print(p)
"""


#Writing the objects created into a csv file 

with open("personas.csv", "w", newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for persona in people:
        writer.writerow(persona.to_dict())
