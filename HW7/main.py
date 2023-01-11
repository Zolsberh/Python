import random
from typing import List


class Animal:

    sex_List: List[str] = ('F', 'M')

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex.upper()

    def __str__(self):
        if self.sex == 'M':
            return f'{self.name} is a good boy!'
        return f'{self.name} is a good girl!'

    def __add__(self, other):
        if not isinstance(other, Animal):
            raise ArithmeticError('Добавляемый объект должен быть типом Animal')
        if self.sex == other.sex:
            raise ValueError('Животные должны быть разнополыми')
        return self.__get_offspring()

    @staticmethod
    def get_info_offspring(offsprings: List['Animal']):
        info: str = '['
        for animal in offsprings:
            info += f'{animal.__class__.__name__}'
            info += f'(name=\'{animal.name}\', age={animal.age}, sex=\'{animal.sex}\')'
            if animal != offsprings[-1]:
                info += ', '
        info += ']'
        return info

    @classmethod
    def __get_offspring(cls):
        offspring = [cls('No name', 0, sex=random.choice(cls.sex_List)) for x in range(random.randint(1, 8))]
        return offspring

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) == 0 or not isinstance(value, str):
            raise TypeError('Имя должно быть строкой и не должно быть пустым')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Возраст должен быть числом и не может быть меньше нуля')
        self.__age = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value: str):
        if not isinstance(value, str) or value not in self.sex_List:
            raise ValueError('Пол не может быть пустым и должен обозначаться как \'F\' или \'M\'')
        self.__sex = value


class Cat(Animal):

    def __add__(self, other):
        if not isinstance(other, Cat):
            raise ArithmeticError('Кота нельзя спарить с другим видом животного')
        return super().__add__(other)


class Dog(Animal):

    def __add__(self, other):
        if not isinstance(other, Dog):
            raise ArithmeticError('Собаку нельзя спарить с другим видом животного')
        return super().__add__(other)


c1 = Cat('Tom', 3, 'M')
c2 = Cat('Elsa', 2, 'f')
print(c1)
print(c2)
offspringCats = c1 + c2
print(Cat.get_info_offspring(offspringCats))

print()

d1 = Dog('Tramp', 5, 'M')
d2 = Dog('Lady', 4, 'F')
print(d1)
print(d2)
offspringDogs = d1 + d2
print(Dog.get_info_offspring(offspringDogs))
