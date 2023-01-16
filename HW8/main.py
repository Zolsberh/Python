from abc import abstractmethod


class Shape:

    def __init__(self, color: str):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise TypeError('Цвет должен быть типом \'строка\'')
        self.__color = value

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def shape_information(self):
        pass

    @abstractmethod
    def draw_shape(self):
        pass


class Rectangle(Shape):

    def __init__(self, length: int | float, width: int | float, color: str):
        if Rectangle.__check_value(length) and Rectangle.__check_value(width):
            self.length = length
            self.width = width
        super().__init__(color)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @staticmethod
    def __check_value(value):
        if isinstance(value, (int, float)) and value > 0:
            return True
        raise TypeError('Длина и ширина должны быть положительным числом больше нуля')

    def perimetr(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return round(self.length * self.width, 2)

    def shape_information(self):
        print('===Прямоугольник===')
        print('Длина:', self.length)
        print('Ширина:', self.width)
        print('Цвет:', self.color)
        print('Площадь:', self.area())
        print('Периметр:', self.perimetr())

    def draw_shape(self):
        end_width = int(self.width - 1)
        end_length = int(self.length - 1)

        for i in range(end_width + 1):
            for j in range(end_length + 1):
                if i == 0 or i == end_width or j == 0 or j == end_length:
                    print('* ', end=' ')
                else:
                    print('  ', end=' ')
            print()


class Square(Rectangle):

    def __init__(self, side: int | float, color: str):
        if Square.__check_value(side):
            self.side = side
            super().__init__(side, side, color)

    @staticmethod
    def __check_value(value):
        if isinstance(value, (int, float)) and value > 0:
            return True
        raise TypeError('Сторона должна быть положительным числом и болше нуля')

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value

    def shape_information(self):
        print('\n===Квадрат===')
        print('Сторона:', self.side)
        print('Цвет:', self.color)
        print('Площадь:', self.area())
        print('Периметр:', self.perimetr())


class Triangle(Shape):

    def __init__(self, base: int | float, side_a: int | float, side_b: int | float, color: str):
        self.base = self.side_a = self.side_b = 0
        if Triangle.__check_value(base) and Triangle.__check_value(side_a) and Triangle.__check_value(side_b):
            if Triangle.__is_correct_triangle(base, side_a, side_b):
                self.base = base
                self.side_a = side_a
                self.side_b = side_b
                self.height = self.__get_height()
                super().__init__(color)
            else:
                raise ValueError('Треугольника с такими сторонами не существует')
        else:
            raise TypeError('Стороны треугольника должны быть положительным числом и больше нуля')

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (int, float)) or value < 0:
            return False
        return True

    @staticmethod
    def __is_correct_triangle(a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        return True

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        self.__base = value

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        self.__side_b = value

    def __get_height(self):
        p = (self.base + self.side_a + self.side_b)/2
        s = (p * (p - self.base) * (p - self.side_a) * (p - self.side_b)) ** 0.5
        height = (2 * s) / self.base
        return height

    def __get_big_side(self):
        return self.side_a if self.side_a > self.side_b else self.side_b

    def perimetr(self):
        return self.base + self.side_a + self.side_b

    def area(self):
        return round(self.base * self.height / 2, 2)

    def shape_information(self):
        print('\n===Треугольник===')
        print('Сторона 1:', self.base)
        print('Сторона 2:', self.side_a)
        print('Сторона 3:', self.side_b)
        print('Цвет:', self.color)
        print('Площадь:', self.area())
        print('Периметр:', self.perimetr())

    def draw_shape(self):
        top_triangle = self.__get_big_side()
        m = self.base // 2
        for i in range(top_triangle):
            for j in range(self.base):
                if (j == m and i == 0) or j == m - i or j == m + i or i == top_triangle - 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()


sq = Square(3, 'red')
sq.shape_information()
sq.draw_shape()
print()
rec = Rectangle(7, 3, 'green')
rec.shape_information()
rec.draw_shape()
print()
tr = Triangle(11, 6, 6, 'yellow')
tr.shape_information()
tr.draw_shape()
