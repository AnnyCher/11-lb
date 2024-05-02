def Zadacha_11_1():
    class Restraurant:
        def __init__(self, restraurant_name='', cuisine_type=''):
            self.restraurant_name = restraurant_name
            self.cuisine_type = cuisine_type

        def describe_restraurant(self):
            print(f'Название ресторана: {self.restraurant_name}')
            print(f'Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Ресторан открыт!')

    newRestraurant = Restraurant()
    newRestraurant.restraurant_name = 'Английский дворик'
    newRestraurant.cuisine_type = 'Европейская'
    newRestraurant.describe_restraurant()
    newRestraurant.open_restaurant()
# Zadacha_11_1()


def Zadacha_11_2():
    class Restraurant:
        def __init__(self, restraurant_name='', cuisine_type=''):
            self.restraurant_name = restraurant_name
            self.cuisine_type = cuisine_type

        def describe_restraurant(self):
            print(f'Название ресторана: {self.restraurant_name}')
            print(f'Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Ресторан открыт!')

    newRestraurant1 = Restraurant()
    newRestraurant1.restraurant_name = 'Английский дворик'
    newRestraurant1.cuisine_type = 'Европейская'

    newRestraurant2 = Restraurant()
    newRestraurant2.restraurant_name = 'Кацо'
    newRestraurant2.cuisine_type = 'Грузинская'

    newRestraurant3 = Restraurant()
    newRestraurant3.restraurant_name = 'Kioko Izakaya'
    newRestraurant3.cuisine_type = 'Паназиатская'

    newRestraurant1.describe_restraurant()
    newRestraurant2.describe_restraurant()
    newRestraurant3.describe_restraurant()
# Zadacha_11_2()


def Zadacha_11_3():
    class Restraurant:
        def __init__(self, restraurant_name='', cuisine_type='', restraurant_rating=0):
            self.restraurant_name = restraurant_name
            self.cuisine_type = cuisine_type
            self.restraurant_rating = restraurant_rating

        def describe_restraurant(self):
            print(f'Название ресторана: {self.restraurant_name}')
            print(f'Тип кухни: {self.cuisine_type}')

        def update_rating(self, restraurant_rating):
            self.restraurant_rating = restraurant_rating
            print(f'Новый рейтинг ресторана - {restraurant_rating}*')

        def open_restaurant(self):
            print('Ресторан открыт!')

    newRestraurant1 = Restraurant()
    newRestraurant1.restraurant_name = 'Английский дворик'
    newRestraurant1.cuisine_type = 'Европейская'

    newRestraurant2 = Restraurant()
    newRestraurant2.restraurant_name = 'Кацо'
    newRestraurant2.cuisine_type = 'Грузинская'

    newRestraurant3 = Restraurant()
    newRestraurant3.restraurant_name = 'Kioko Izakaya'
    newRestraurant3.cuisine_type = 'Паназиатская'

    newRestraurant1.update_rating(input('Введите рейтинг ресторана (от 1 до 5)\n'))
    newRestraurant2.update_rating(input('Введите рейтинг ресторана (от 1 до 5)\n'))
    newRestraurant3.update_rating(input('Введите рейтинг ресторана (от 1 до 5)\n'))
Zadacha_11_3()
