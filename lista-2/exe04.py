grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))

def calculator():
    average = (grade1 + grade1) / 2

    if average >= 7:
        print("Aprovado")
    elif 5 >= average <= 6.9:
        print("Recuperação")
    else:
        print("Reprovado")
calculator()
