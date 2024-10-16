"""Oppgave 3 - Funksjon - Printe liste"""


def print_list(liste: list):
    """Funksjon: printe ut hvert element i liste gitt som parameter"""
    for element in liste:
        print(element)


mat = ["Skirt steak sandwich", "Burritos", "Biff med fløtegratinerte poteter"]

print_list(mat)
