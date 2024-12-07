


class Plant:   # это родительский класс
    edible = False  # съедобность
    def __init__(self,name): #
        self.name = name

class Animal:  # это родительский класс
    alive = True  # живой
    fed = False    # накормленный
    def __init__(self,name):
        self.name = name

    def eat(self, food: Plant):
        if food.edible: # если переданное растение съедобное
            print(f'{self.name} съел {food.name}')
            self.fed = True # о значение fed меняется на True
        else:
            print(f'{self.name} не стал есть {food.name}') # если растение не съедобное
            self.alive = False# то значение alive переопределяется на  False

class Mammal(Animal):  # дочерний класс Animal
    pass

class Predator(Animal):  #дочерний класс Animal
   pass

class Flower(Plant):  #дочерний класс Plant
   pass

class Fruit(Plant):  #дочерний класс Plant
  edible = True #  переопределяем значение съедобности на True

a1 = Predator('Тигр Шерхан')
a2 = Mammal('Кот Базилио')
p1 = Flower('Лютик')
p2 = Fruit('Синьор Помидор')
print(a1.name)
print(a2.name)
print(p1.name)
print(p2.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
