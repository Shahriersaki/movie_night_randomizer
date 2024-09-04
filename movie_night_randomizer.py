import random
import os
import json

class MovieNightRandomizer:
    def __init__(self, file_name="movies.json"):
        self.file_name = file_name
        self.movies = []
        self.load_movies()

    def load_movies(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                self.movies = json.load(f)

    def save_movies(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.movies, f, indent=4)

    def add_movie(self, title, genre):
        self.movies.append({'title': title, 'genre': genre})
        self.save_movies()

    def view_movies(self):
        if not self.movies:
            print("No movies in the list.")
        else:
            for i, movie in enumerate(self.movies, 1):
                print(f"{i}. {movie['title']} ({movie['genre']})")

    def remove_movie(self, index):
        if 0 <= index < len(self.movies):
            removed_movie = self.movies.pop(index)
            print(f"Removed: {removed_movie['title']}")
            self.save_movies()
        else:
            print("Invalid index.")

    def random_movie(self, genre=None):
        if genre:
            genre_movies = [movie for movie in self.movies if movie['genre'].lower() == genre.lower()]
            if genre_movies:
                return random.choice(genre_movies)
            else:
                print(f"No movies found for genre: {genre}")
                return None
        else:
            if self.movies:
                return random.choice(self.movies)
            else:
                print("No movies in the list.")
                return None

def main():
    randomizer = MovieNightRandomizer()

    while True:
        print("\nMovie Night Randomizer")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Remove Movie")
        print("4. Random Movie")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            randomizer.add_movie(title, genre)

        elif choice == "2":
            randomizer.view_movies()

        elif choice == "3":
            randomizer.view_movies()
            index = int(input("Enter the number of the movie to remove: ")) - 1
            randomizer.remove_movie(index)

        elif choice == "4":
            genre = input("Enter genre (or leave blank to choose from all movies): ")
            movie = randomizer.random_movie(genre)
            if movie:
                print(f"Random Movie: {movie['title']} ({movie['genre']})")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
