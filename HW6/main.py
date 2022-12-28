class Student:

    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise TypeError('Имя не должно быть пустым и должно иметь строковый тип')
        self.__name = value

    @property
    def laptop(self):
        return self.__laptop

    @laptop.setter
    def laptop(self, value):
        if not isinstance(value, self.Laptop):
            raise TypeError('Ноутбук должен быть типом Laptop')
        self.__laptop = value

    def display(self):
        print(f'{self.name} =>', end=' ')
        self.laptop.display()

    class Laptop:

        def __init__(self):
            self.model = 'HP'
            self.cpu = 'i7'
            self.ram = 16

        def display(self):
            print(f'{self.model},{self.cpu}, {self.ram}')


s1 = Student('Roman')
s2 = Student('Vladimir')
s1.display()
s2.display()
