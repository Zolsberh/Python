import math


class Table:

    def __init__(self, length=None, width=None, radius=None):
        self.length = length
        self.width = width
        self.radius = radius

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value is not None:
            self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value is not None:
            self._width = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value is not None:
            self._radius = value

    def table_area(self):
        raise NotImplemented('В дочернем классе должен быть реалезован метод table_area()')


class RectangleTable(Table):

    def __init__(self, length, width):
        super().__init__(length, width)

    def table_area(self):
        return self.length * self.width


class RoundTable(Table):

    def __init__(self, radius):
        super().__init__(None, None, radius)

    def table_area(self):
        return round(math.pi * self.radius ** 2, 2)


desk1 = RectangleTable(20, 10)
desk2 = RectangleTable(20, 20)
desk3 = RoundTable(20)

print(desk1.__dict__)
print(desk1.table_area())
print(desk2.__dict__)
print(desk2.table_area())
print(desk3.__dict__)
print(desk3.table_area())

