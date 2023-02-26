from model import MovieModel
from view import UserInterface


class Controller:

    def __init__(self) -> None:
        self.movie_model = MovieModel()
        self.user_interface = UserInterface()

    def run(self) -> None:
        answer = None
        while answer != 'q':
            answer = self.user_interface.show_selection_options()
            self.check_answer_user(answer)

    def check_answer_user(self, answer: str) -> None:
        if answer == "1":
            movie = self.user_interface.add_user_movie()
            self.movie_model.add_movie(movie)
        elif answer == "2":
            movies = self.movie_model.get_all_movies()
            self.user_interface.show_all_movies(movies)
        elif answer == "3":
            movie_name = self.user_interface.get_movie()
            try:
                movie = self.movie_model.get_movie(movie_name)
            except KeyError:
                self.user_interface.show_incorrect_name_error(movie_name)
            else:
                self.user_interface.show_movie(movie)
        elif answer == "4":
            movie_name = self.user_interface.get_movie()
            try:
                movie = self.movie_model.get_movie(movie_name)
            except KeyError:
                self.user_interface.show_incorrect_name_error(movie_name)
            else:
                self.user_interface.remove_movie(movie)
        elif answer == "q":
            self.movie_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)
