def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def show_selection_options(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title('Добавление фильма:')
    def add_user_movie(self):
        dict_movies = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_movies:
            if key == "режиссер":
                attr = "режиссера"
                dict_movies[key] = input(f"Введите {attr} фильма: ")
            elif key == "студия":
                attr = "студию"
                dict_movies[key] = input(f"Введите {attr} фильма: ")
            elif key == "актеры":
                attr = "актеров"
                try:
                    input_str = input(f"Введите {attr} фильма через запятую: ")
                    str_actors = input_str.split(',')
                    dict_movies[key] = str_actors
                except ValueError:
                    print("Не корректный ввод")
            elif key == "год выпуска":
                attr = key
                try:
                    dict_movies[key] = int(input(f"Введите {attr} фильма: "))
                except ValueError:
                    print("Не корректный ввод")
            elif key == "длительность":
                attr = key
                try:
                    dict_movies[key] = int(input(f"Введите {attr} фильма: "))
                except ValueError:
                    print("Не корректный ввод")
            else:
                attr = key
                dict_movies[key] = input(f"Введите {attr} фильма: ")
        return dict_movies

    @add_title('Каталог фильмов:')
    def show_all_movies(self, movies):
        for ind, movie in enumerate(movies, start=1):
            print(f"{ind}. {movie}")

    @add_title('Ввод названия фильма:')
    def get_movie(self):
        movie_name = input("Введите название фильма: ")
        return movie_name

    @add_title('Просмотр фильма:')
    def show_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @add_title('Сообщение об ошибке:')
    def show_incorrect_name_error(self, movie_name):
        print(f"Фильма с названием {movie_name} не существует")

    @add_title('Удаление фильма:')
    def remove_movie(self, movie):
        print(f"Статья {movie} - был удален")

    @add_title('Сообщение об ошибке:')
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")
