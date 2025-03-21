words = {'Água': 'Water', 'Carro': 'Car', 'Azul': 'Blue'}

word = input("Expresse uma palavra em português: ")

if word in words:
  print(f"Tradução de {word} é {words[word]}.")
else:
  print("Tradução Indisponível.")
