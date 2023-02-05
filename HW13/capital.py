class Capital:

    def __init__(self, country: str, city: str):
        self.country = country
        self.city = city

    @staticmethod
    def __check_value(val: str) -> bool:
        if not isinstance(val, str):
            raise TypeError('name must be string')
        if not val[0].isupper():
            raise ValueError('name must start with capital letter')
        return True

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, val) -> None:
        if Capital.__check_value(val):
            self.__country = val

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, val) -> None:
        if Capital.__check_value(val):
            self.__city = val
