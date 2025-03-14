def contador_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador


palavra = input("Expresse uma palavra: ")
numero_vogais = contador_vogais(palavra)
print(f"A palavra '{palavra}' contém {numero_vogais} vogais.")
