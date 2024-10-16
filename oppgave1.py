"""Oppgave 1 - Dictionaries"""

student = {
    "first name": "Stian",
    "last name": "Hetsch",
    "favorite course": "Programmering 1",
}

student["favorite course"] = "ITF10219 Programmering 1"

student.update({"age": "38"})

print(f"{student['first name']} {student['last name']}")
