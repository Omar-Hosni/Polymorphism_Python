
class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"


class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

rex = Dog("Rex")
felix = Cat("Felix")

print(rex.speak())
print(felix.speak())

print("\n" + 'printing using for loop')

for pet_class in [rex,felix]:
    print(pet_class.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(rex)
