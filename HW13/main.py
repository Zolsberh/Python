from capital import Capital
from editor_of_capitals import EditorOfCapitals


class ActionError(ValueError):
    def __init__(self):
        super().__init__('выбор должен быть целым число от 1 до 6')


def check_enter():
    try:
        print('*'*30)
        print('Выбор действия:')
        print('1 - добавление данных')
        print('2 - удаление данных')
        print('3 - поиск данных')
        print('4 - редактирование данных')
        print('5 - просмотр данных')
        print('6 - завершение работы')
        val = int(input('Ввод: '))
        if val not in [1, 2, 3, 4, 5, 6]:
            raise ActionError
        return val
    except ValueError:
        raise ActionError


filename = 'capitals.json'
action = 0

while action != 6:
    try:
        action = check_enter()
        if action == 1:
            country = input('Введите название страны (с заглавной буквы): ')
            city = input('Введите название столицы страны (с заглавной буквы): ')
            capital = Capital(country, city)
            EditorOfCapitals.add_capital(filename, capital)
        if action == 2:
            country = input('Введите название страны (с заглавной буквы): ')
            capital = EditorOfCapitals.delete_capital(filename, country)
            print(f'Из данных удалена страна {country} со столицей {capital}')
        if action == 3:
            country = input('Введите название страны (с заглавной буквы): ')
            capital = EditorOfCapitals.search_capital(filename, country)
            print(f'В стране {country} столица {capital}')
        if action == 4:
            country = input('Введите название страны (с заглавной буквы): ')
            city = input('Введите название столицы страны (с заглавной буквы): ')
            EditorOfCapitals.edit_capital(filename, country, city)
            print(f'В стране {country} изменена столица на {city}')
        if action == 5:
            print(EditorOfCapitals.get_data(filename))
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except KeyError as ke:
        print(ke)

