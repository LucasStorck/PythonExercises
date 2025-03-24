def banco():
  try:
    saldo = 1000
    valor_saque = int(input("Qual o valor do saque?: "))

    if valor_saque > saldo:
      print("Saldo Insuficiente!")
    else:
      saldo -= valor_saque
      print(f"Saque no valor de {valor_saque} realizado com sucesso!")
  except ValueError:
    print("Informe um valor válido para saque!")


banco()
