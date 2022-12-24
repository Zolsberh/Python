class Auto:

    def __init__(self, model, year, manufacturer, engin, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engin = engin
        self.color = color
        self.price = price

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def engin(self):
        return self.__engin

    @property
    def color(self):
        return self.__color

    @property
    def price(self):
        return self.__price

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError('Название модели должно быть строкой')
        self.__model = value

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError('Год должен быть числом')
        self.__year = value

    @manufacturer.setter
    def manufacturer(self, value):
        if not isinstance(value, str):
            raise TypeError('Название производителя долнобыть строкой')
        self.__manufacturer = value

    @engin.setter
    def engin(self, value):
        if not isinstance(value, int):
            raise TypeError('Мощность двигателя должна быть числом')
        self.__engin = value

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise TypeError('Цвет должен быть строкой')
        self.__color = value

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError('Цена должна быть числом')
        self.__price = value

    def print_info(self):
        print('*'*10, 'Дaнные автомобиля', '*'*10)
        print('Название модели:', self.model)
        print('Год выпуска:', self.year)
        print('Производитель:', self.manufacturer)
        print(f'Мощность двигателя: {self.engin} л.с.')
        print('Цвет машины:', self.color)
        print('Цена:', self.price)
        print('='*40)


auto = Auto('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)
auto.print_info()
