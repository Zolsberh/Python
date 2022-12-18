class Calculation:

    __counter = 0

    @staticmethod
    def increase_counter():
        Calculation.__counter += 1

    @staticmethod
    def get_counter():
        return Calculation.__counter

    @staticmethod
    def square_of_triangle_to_heron(side_a, side_b, side_c):
        p = (side_a + side_b + side_c)/2
        square = (p * (p - side_a) * (p - side_b) * (p - side_c)) ** 0.5
        Calculation.increase_counter()
        return square

    @staticmethod
    def square_of_triangle_classic(base, height):
        square = (base * height) * 0.5
        Calculation.increase_counter()
        return square

    @staticmethod
    def square_of_quadrat(side):
        Calculation.increase_counter()
        return side * side

    @staticmethod
    def square_of_rectangle(side_a, side_b):
        Calculation.increase_counter()
        return side_a * side_b


print('Площадь треугольника по формуле Герона (3, 4, 5):', Calculation.square_of_triangle_to_heron(3, 4, 5))
print('Площадь треугольника через основание и высоту (6, 7):', Calculation.square_of_triangle_classic(6, 7))
print('Площадь квадарата (7)', Calculation.square_of_quadrat(7))
print('Площадь прямоугольника (2, 6):', Calculation.square_of_rectangle(2, 6))
print('Количество подсчетов площади:', Calculation.get_counter())
