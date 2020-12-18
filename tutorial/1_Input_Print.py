class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('My name is ' + self.name + ' and my age is ' + str(self.age))

hb = Person('HarryBro', 20)
hb.introduce()
