students = {}

for i in range(3):
  name = input("Qual o nome do aluno?: ")
  grade = float(input("Qual a nota do aluno?: "))
  students[name] = grade

print(students)
