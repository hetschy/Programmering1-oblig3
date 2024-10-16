"""Oppgave 5.3 - Skrive/leste til fil"""

filmer: list[dict] = []


def add_movie(name: str, year: int, rating=5.0):
    """Funksjon: legger film til liste"""
    movie = {"name": name, "year": year, "rating": rating}
    filmer.append(movie)


def print_movies(movies: list):
    """Funksjon: printer filmer i liste: {title} - {year} {rating}"""
    for movie in movies:
        print(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}")


def average(movies: list):
    """Funksjon: returnerer average rating for filmer i liste"""
    rating_sum: float = 0
    for movie in movies:
        rating_sum += movie["rating"]
    return round(rating_sum / len(movies), 2)


def get_movies(movies: list, year: int):
    """Funksjon: returnerer liste av filmer fra og med gitt årstall"""
    year_liste = [movie for movie in movies if movie["year"] >= year]
    return year_liste


def write_file(movies: list, fn: str):
    """Funksjon: skriver liste til fil"""
    with open(fn, "w") as f:
        for movie in movies:
            f.write(f"{movie['name']} - {movie['year']}, rating: {movie['rating']}\n")


def read_file(fn: str):
    """Funksjon: leser fil"""
    with open(fn, "r") as f:
        print(f.read())


add_movie("Joker: Folie à Deux", 2024, 5.3)
add_movie("The Dark Knight", 2008, 9.0)
add_movie("Fight Club", 1999, 8.8)
add_movie("Interstellar", 2014)

nyere_filmer = get_movies(filmer, 2008)

write_file(nyere_filmer, "filmer.txt")

read_file("filmer.txt")
