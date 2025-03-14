def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

numeros = input("Expresse alguns número: ")
listaNumeros = [float(num) for num in numeros.split()]

media = calcular_media(listaNumeros)
print(f"Média dos números digitados: {media}")