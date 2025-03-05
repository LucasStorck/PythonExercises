from multiprocessing.reduction import duplicate

numbers = []

qtd = int(input("Home many numbers? "))

for i in range(qtd):
    number = int(input("Number: "))
    numbers.append(number)

duplicatedNumber = list(set(numbers))

print("Original List: ", numbers)
print("New List: ", duplicatedNumber)