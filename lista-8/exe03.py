def conversao():
  try:
    numero = int(input("Expresse um Número Inteiro: "))
    resultado = numero * 2
  except ValueError:
    print("O Número precisa ser do tipo inteiro!")
  except TypeError:
    print("Precisa ser um número!")
  else:
    print(f"O Resultado é: {resultado}")
  finally:
    print("Feito!")


conversao()
