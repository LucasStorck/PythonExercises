def acesso_elementos():
  numeros = [20, 40, 60, 80, 100, 120, 140, 160, 180]

  try:
    indice = int(input("Informe um índice para acessar um valor da lista (0 a 8): "))

    valor = numeros[indice]

    print(f"O valor no índice {indice} é: {valor}")

  except IndexError:
    print("O índice informado não existe!")
  except ValueError:
    print("O número do índice precisa ser do tipo inteiro!")


acesso_elementos()
