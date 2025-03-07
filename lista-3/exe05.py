n = int(input("Expresse um número N: "))

a, b = 0, 1

print("Seqência de Fibonacci")

for _ in range(n):
    print(a, end="")
    a, b = b, a + b
