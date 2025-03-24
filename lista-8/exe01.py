def divisao_segura():
  try:
    num_x = float(input("Digite o Numerador: "))
    num_y = float(input("Digite o Denominador: "))
    resultado = num_x / num_y

  except ValueError:
    print("Erro: Número Inválido")

  except ZeroDivisionError:
    print("Erro: Impossível Dividir Números por Zero!")

  else:
    print(f"O Resultado da Divisão é: {resultado}")

  finally:
    print("Feito")
divisao_segura()
