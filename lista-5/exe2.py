number = int(input("Expresse um número inteiro: "))

def verificar_numero_primo(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
if verificar_numero_primo(number):
    print(f"O número {number} é primo!")
else:
    print(f"O número {number} não é primo!")