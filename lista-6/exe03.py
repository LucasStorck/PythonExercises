rainbow_colors = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")

number = int(input("Digite um número de 1 a 1 para ver a cor correspondente do Arco-Íris: "))

if 1 <= number <=7:
    color = rainbow_colors[number-1]
    print(f"Com base no número digitado, a cor correspondente é: {color}")
else:
    print("Número inválido! O número deve estar entre 1 a 7")
