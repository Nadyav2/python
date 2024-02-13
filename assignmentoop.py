class person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def show(self):
        print(f"My name is {self.name}"
              f" and I am {self.age} years old.")

myper = person("kenza", 19)
myper2 = person("Duke", 18)
myper3 = person("Mikey", 21)
myper4 = person("Drako", 29)
myper5 = person("Rema", 24)
myper.show()
myper2.show()
myper3.show()
myper4.show()
myper5.show()