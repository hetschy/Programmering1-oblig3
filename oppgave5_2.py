"""Oppgave 5.2 - Mer Funksjoner"""

filmer: list[dict] = []


def add_movie(filmliste: list[dict], name: str, year: int, rating=5.0):
    """Funksjon: legger film til liste"""
    movie = {"name": name, "year": year, "rating": rating}
    filmliste.append(movie)


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


add_movie(filmer, "Joker: Folie à Deux", 2024, 5.3)
add_movie(filmer, "The Dark Knight", 2008, 9.0)
add_movie(filmer, "Fight Club", 1999, 8.8)
add_movie(filmer, "Interstellar", 2014)

print(average(filmer))

nyere_filmer = get_movies(filmer, 2008)

print_movies(nyere_filmer)
