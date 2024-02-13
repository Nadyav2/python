class Fruits:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

    def onyesha(self):
        print(f"My favourite fruit is {self.name}"
              f" and its costs Ksh. {self.price}"
              f" and its colour {self.colour}")


myobj = Fruits("Orange", 50, "orange")
myobj = Fruits("Pineapple", 350, "Yellow")
myobj = Fruits("Grape", 5450, "Purple")
myobj.onyesha()
