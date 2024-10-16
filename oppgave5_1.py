"""Oppgave 5.1 - Dictionaries og Funksjoner"""

inception = {"name": "Inception", "year": 2010, "rating": 8.7}
inside_out = {"name": "Inside Out", "year": 2015, "rating": 8.1}
con_air = {"name": "Con Air", "year": 1997, "rating": 6.9}

filmer = []

filmer.append(inception)
filmer.append(inside_out)
filmer.append(con_air)


def add_movie(filmliste: list[dict], name: str, year: int, rating=5.0):
    """Funksjon: tar liste og film, legger film til liste"""
    movie = {"name": name, "year": year, "rating": rating}
    filmliste.append(movie)


add_movie(filmer, "Joker: Folie à Deux", 2024, 5.3)
add_movie(filmer, "The Dark Knight", 2008, 9.0)
add_movie(filmer, "Fight Club", 1999, 8.8)
add_movie(filmer, "Interstellar", 2014)
