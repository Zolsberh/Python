import json
from random import choice
from typing import Dict


class RandomObject:
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    @staticmethod
    def __to_dict() -> Dict[str, str]:
        name = ''.join([choice(RandomObject.letters) for x in range(7)])
        tel = ''.join([choice(RandomObject.numbers) for x in range(10)])
        dict_of_human = {
            'name': name,
            'tel': tel
        }
        return dict_of_human

    @staticmethod
    def __checking_file(filename: str) -> Dict[str, Dict[str, str]]:
        try:
            fr = open(filename)
            data = json.load(fr)
        except FileNotFoundError:
            data = {}
        return data

    @staticmethod
    def __writing_to_file(filename: str, data: Dict[str, Dict[str, str]]) -> None:
        with open(filename, 'w') as fp:
            json.dump(data, fp, indent=2)

    @staticmethod
    def add_to_json(filename: str) -> None:
        data = RandomObject.__checking_file(filename)
        id_obj = ''.join([choice(RandomObject.numbers) for x in range(10)])
        data.setdefault(id_obj, RandomObject.__to_dict())
        RandomObject.__writing_to_file(filename, data)

    @staticmethod
    def remove_from_json(file: str) -> None:
        data = RandomObject.__checking_file(file)
        if len(data) > 0:
            data.popitem()
        else:
            raise IndexError('список пуст. Невозможно удалить из пустого списка')
        RandomObject.__writing_to_file(file, data)
