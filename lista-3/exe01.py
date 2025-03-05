numbers = []

qtd = int(input("How many numbers?: "))

for i in range(qtd):
    number = int(input("Number: "))
    numbers.append(number)

soma = sum(numbers)

print("Numbers Sum: ", soma)
