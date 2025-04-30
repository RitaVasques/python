import os

class Movie:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def write_movie(self):
        return self.name

class ManageMovies:
    file_name = 'movies.txt'
    
    def __init__(self):
        self.movies = []
        if os.path.isfile(self.file_name):
            self.movies = self.read_movies_file()
    
    def save_movies_in_file(self, movies):
        try:
            with open(self.file_name, 'a') as file:
                for movie in movies:
                    file.write(f'{movie.write_movie()}\n')
        except Exception as e:
            print(f'Error saving movie: {e}')
    
    def read_movies_file(self):
        movies = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    name = line.strip()
                    movie = Movie(name)
                    movies.append(movie)
        except Exception as e:
            print(f'Error reading file: {e}')
        return movies

    def add_movie(self, movie):
        self.movies.append(movie)
        self.save_movies_in_file([movie])

    def show_movies(self):
        if os.path.isfile(self.file_name):
            print('\n')
            print('----Available Movies---')
            for movie in self.movies:
                print(movie)
            print('\n')
        else:
            print(f'{self.file_name} not found')
    
    def getMovies(self):
        return self.movies
    
    def delete_file(self):
        try:
            if os.path.isfile(self.file_name):
                os.remove(self.file_name)
                self.movies = [] #Clear in memory movies
                print(f'{self.file_name} was deleted')
        except Exception as e:
            print(f'Error deleting the file {self.file_name}: {e}')

class AppMovies:
    def __init__(self):
        self.manage_movies = ManageMovies()

    def app_movies(self):
        exit = False
        print('*** App Movies ***')
        print('''Options:
              1. Add Movie
              2. Show Movies
              3. Delete catalog
              4. Exit''')
        return int(input('Chose an option: '))
    
    def execute_option(self, option):
        if option == 1:
            self.add_movie()
        elif option == 2:
            self.manage_movies.show_movies()
        elif option == 3:
            self.manage_movies.delete_file()
        elif option == 4:
            print('Bye Bye')
            return True
        else:
            print('Not a valid option')
        return False

    def add_movie(self):
        name = input('Movie name: ')
        movie = Movie(name)
        self.manage_movies.add_movie(movie)
        print(f'{name} added')

if __name__ == '__main__':
    app = AppMovies()
    while True:
        try:
            option = app.app_movies()
            should_exit = app.execute_option(option)
            if should_exit:
                break
        except Exception as e:
            print(f'An Error occurred: {e}')