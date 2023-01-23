class Integer:

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(f'value {self.__name} must be integer and greater than zero')
        instance.__dict__[self.__name] = value


class Triangle:

    side_a = Integer()
    side_b = Integer()
    side_c = Integer()

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_correct_triangle(self):
        info = f'Треугольник со сторонами ({self.side_a}, {self.side_b}, {self.side_c})'
        if (self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b
                or self.side_b + self.side_c <= self.side_a):
            print(info + ' не существует')
        else:
            print(info + ' существует')


tr1 = Triangle(2, 5, 6)
tr2 = Triangle(5, 2, 8)
tr3 = Triangle(7, 3, 6)

triangles = [tr1, tr2, tr3]

for tr in triangles:
    tr.is_correct_triangle()
