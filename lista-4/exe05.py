numbers = []

qtd = int(input("How many numbers?: "))

for i in range(qtd):
    number = int(input("Number: "))
    numbers.append(number)

for num in set(numbers):
    count = numbers.count(num)
    print(f"The number {num} appears {count} times")
