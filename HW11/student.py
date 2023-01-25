class NameDescriptor:

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or value == "" or self.__is_there_number_in_name(value):
            raise ValueError('некорректный ввод имени. Имя не должно быть пустым и содержать цифры')
        instance.__dict__[self.__name] = value

    @staticmethod
    def __is_there_number_in_name(value):
        for s in value:
            if s.isdigit():
                return True
        return False


class Student:
    firstname = NameDescriptor()
    lastname = NameDescriptor()

    def __init__(self, firstname: str, lastname: str, age: int, group: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.group = group

    def __str__(self):
        return f'Имя: {self.firstname}, Фамилия: {self.lastname}, Возраст: {self.age}, Группа: {self.group}'

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError('возраст должен быть целым числом и не меньше нуля')
        self.__age = value

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, value) -> None:
        if not isinstance(value, str) or value == "":
            raise ValueError('некорректный ввод названия группы')
        self.__group = value
