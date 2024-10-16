"""Oppgave 2 - Funksjon - Tallgenerering"""

from random import randrange


def rand_print():
    """Funksjon: printe ut tilfeldig tall mellom 0 og 100 (center padding)"""
    print("--------------------")
    print(f"---- {randrange(0, 100):^10} ----")
    print("--------------------")


for n in range(randrange(3, 6)):
    rand_print()
