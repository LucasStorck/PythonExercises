names_grades = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9, 2, 'Daniel', 6.8, 'Eduarda', 8.0)

for name in names_grades:
    if isinstance(name, str):
        print(f"Nome dos Alunos: {name}")

for grade in names_grades:
    if isinstance(grade, float):
        print(f"Nota dos Alunos: {grade}")
