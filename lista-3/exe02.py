soma = 0

while True:
    number = int(input("Number: "))

    if number < 0:
        break
    if number > 0:
        soma += number
print(f"Sum: {soma}")
