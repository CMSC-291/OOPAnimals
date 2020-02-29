from animals import Dog, Cat, Meal

from newRepo.animals import Chiweenie

if __name__ == '__main__':
    charlie = Chiweenie("Chuck", 9)
    jules = Cat()
    meal = Meal("table scraps", 200)

    charlie.eat(meal)
    jules.eat(meal)
    print(jules.lives)
    print(jules.meals_eaten)

    jules.play()
    charlie.play()
    a = None.run()