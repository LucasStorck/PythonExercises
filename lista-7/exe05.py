words = {'Água': 2015, 'Caderno': 2520, 'Borracha': 3025}

code = int(input("Digite o código do produto: "))

for product, product_code in words.items():
  if product_code == code:
    print(f"O código do produto {product} é {code}.")
    break
else:
  print("Produto Indisponível.")
