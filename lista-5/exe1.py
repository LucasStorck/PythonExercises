number = int(input("Exprese um número inteiro: "))

def calcular_fatorial(resultado = 1, contador = 1):
    while contador <= number:
        resultado *= contador
        contador += 1
    return resultado

print(calcular_fatorial())
