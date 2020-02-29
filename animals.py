class Meal:
    def __init__(self, name, calories=250):
        self.name = name
        self.calories = calories


class Animal:
    def __init__(self):
        self.meals_eaten = []

    def eat(self, food: Meal):
        self.meals_eaten.append(food)
        print("I eat {}".format(food.name))

    def play(self):
        print("playtime!")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.lives = 9

    def purr(self):
        print("Purr")
        self.walk()

    def walk(self):
        print("Bebop around.")

    def play(self):
        print("I pounce!")
        super().play()


class Dog(Animal):
    def __init__(self, name="DEFAULTO", age: float = 3.0):
        super().__init__()
        self.age = age
        self.name = name

    def bark(self, loudness):
        if loudness < 0.5:
            print("Ruff!")
        else:
            print("BOWWOWOWOWOWOW")

    def snuggle(self):
        print("Get cuddly, " + self.name)

    def sleep(self):
        self.snuggle()
        if self.age < 4:
            print("zzzzz")
        else:
            print("ZZZZZZZZZZZZZ")
        return "rested"

    def walk(self):
        print("Bebop around.")

class Chiweenie(Dog):
    def __init__(self, name="DEFAULTO", age: float = 3.0):
        super().__init__(name, age)
        self.napolean_complex = True