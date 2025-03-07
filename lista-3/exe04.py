a = int(input("Número A: "))
b = int(input("Número B: "))

if a > b:
    a, b = b, a

print(f"Números Imprares: {a} a {b}")
for number in range(a, b + 1):
    if number % 2 != 0:
        print(number)
