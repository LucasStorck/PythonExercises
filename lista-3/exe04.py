numbers = []

qtd = int(input("How many numbers?: "))

for i in range(qtd):
    number = int(input("Number: "))
    numbers.append(number)

inverted = list(reversed(numbers))

print("Original List: ", numbers)
print("Inverted List: ", inverted)
