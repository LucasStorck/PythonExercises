numbers = []

qtd = int(input("How many numbers?: "))

for i in range(qtd):
    number = int(input("Number: "))
    numbers.append(number)

maxNumber = max(numbers)
minNumber = min(numbers)

print("Max Number: ", maxNumber)
print("Min Number: ", minNumber)
