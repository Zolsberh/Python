import pickle
import os


class ActorsListError(ValueError):
    def __init__(self):
        super().__init__('value must be list with strings')


class Movie:

    def __init__(self, name: str, genre: str, director: str, year: int, duration: int,
                 studio: str, actors: list[str]) -> None:
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.name} ({self.year})'

    @property
    def actors(self) -> list[str]:
        return self.__actors

    @actors.setter
    def actors(self, value) -> None:
        if not isinstance(value, list):
            raise ActorsListError
        for s in value:
            if not isinstance(s, str):
                raise ActorsListError
        self.__actors = value


class MovieModel:

    def __init__(self):
        self.db_name = 'db.txt'
        self.movies_dict = self.load_data()

    def add_movie(self, dict_movies: dict) -> None:
        movie = Movie(*dict_movies.values())
        self.movies_dict[movie.name] = movie

    def get_all_movies(self):
        return self.movies_dict.values()

    def get_movie(self, movie_name):
        movie = self.movies_dict[movie_name]
        dict_movies = {
            "название": movie.name,
            "жанр": movie.genre,
            "режиссер": movie.director,
            "год выпуска": movie.year,
            "длительность": f"{movie.duration} мин",
            "студия": movie.studio,
            "актеры": ",".join(movie.actors)
        }
        return dict_movies

    def remove_movie(self, movie_name):
        return self.movies_dict.pop(movie_name)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.movies_dict, f)
