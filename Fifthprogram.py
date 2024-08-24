class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

p1 = Person("John",26)
p2 = Person("Mohan",21)
print("Person name and age",p1.name,p1.age)
print("Person name and age",p2.name,p2.age)
    
for i in p1.name:
    print(i)
for i in p2.name:
    print(i)
    