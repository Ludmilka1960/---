


class Vehicle:
    __COLOR_VARIANTS =  'BLUE', 'BLACK', 'GREEN'
    def __init__(self,owner, model,engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
       print(self.get_model())
       print(self.get_horsepower())
       print(self.get_color())
       print(f'Владелец: {self.owner}')

    def set_color(self,new_color):

        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color

        else:
            print( "Нельзя сменить цвет на 'new_color'")


class Sedan(Vehicle):
     __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Пупсик', 'Toyota EHO', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('pink')
vehicle1.set_color('black')
vehicle1.owner='Красотка'
vehicle1.print_info()



