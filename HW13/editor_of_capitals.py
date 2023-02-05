from capital import Capital
from typing import Dict
import json


class EditorOfCapitals:

    __info = dict()

    @staticmethod
    def __check_capital(capital) -> bool:
        if not isinstance(capital, Capital):
            raise TypeError('value must be an object of the capital class')
        return True

    @staticmethod
    def __check_key(val) -> bool:
        if not isinstance(val, str) or not val[0].isupper():
            raise ValueError('name country must be string and start with capital letter')
        list_countries = list(EditorOfCapitals.__info.keys())
        if val not in list_countries:
            raise KeyError('there is no country with this name in the dictionary')
        return True

    @staticmethod
    def __check_file(filename: str) -> None:
        try:
            f = open(filename)
            EditorOfCapitals.__info = json.load(f)
        except FileNotFoundError:
            pass

    @staticmethod
    def __write_to_file(filename: str) -> None:
        with open(filename, 'w') as fw:
            json.dump(EditorOfCapitals.__info, fw, ensure_ascii=False, indent=2)
        print('Файл сохранен')

    @staticmethod
    def __read_from_file(filename: str) -> None:
        with open(filename, 'r') as fr:
            EditorOfCapitals.__info = json.load(fr)

    @staticmethod
    def add_capital(filename: str, capital: Capital) -> None:
        EditorOfCapitals.__check_file(filename)
        if EditorOfCapitals.__check_capital(capital):
            list_countries = list(EditorOfCapitals.__info.keys())
            if capital.country in list_countries:
                raise KeyError('country with this name is already in the dictionary')
            EditorOfCapitals.__info.setdefault(capital.country, None)
            EditorOfCapitals.__info[capital.country] = capital.city
            EditorOfCapitals.__write_to_file(filename)

    @staticmethod
    def delete_capital(filename: str, country: str) -> str:
        EditorOfCapitals.__check_file(filename)
        if EditorOfCapitals.__check_key(country):
            capital = EditorOfCapitals.__info.pop(country)
            EditorOfCapitals.__write_to_file(filename)
            return capital

    @staticmethod
    def search_capital(filename: str, country: str) -> str:
        EditorOfCapitals.__check_file(filename)
        if EditorOfCapitals.__check_key(country):
            capital = EditorOfCapitals.__info[country]
            return capital

    @staticmethod
    def edit_capital(filename: str, country: str, city: str) -> None:
        EditorOfCapitals.__check_file(filename)
        if not isinstance(city, str) or not city[0].isupper():
            raise ValueError('name city must be string and start with capital letter')
        if EditorOfCapitals.__check_key(country):
            EditorOfCapitals.__info[country] = city
            EditorOfCapitals.__write_to_file(filename)

    @staticmethod
    def get_data(filename: str) -> Dict[str, str]:
        EditorOfCapitals.__read_from_file(filename)
        return EditorOfCapitals.__info
