from typing import Callable


class Power:

    def __init__(self, degree: int | float) -> None:
        if not isinstance(degree, int | float):
            raise TypeError('Degree must be a number')
        self.degree = degree

    def __call__(self, fn: Callable) -> Callable:
        def wrap(*args, **kwargs):
            print('Результат:', fn(*args, *kwargs) ** self.degree)
        return wrap


@Power(3)
def func(a, b):
    return a * b


func(2, 2)
