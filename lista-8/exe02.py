def abrir_arquivo():
  try:
    arquivo = input("Upload do Arquivo: ")
    open(arquivo, "r")

  except FileExistsError:
    print("Erro no Arquivo!")

  except FileNotFoundError:
    print("Arquivo Não Econtrado!")

  finally:
    print("Feito!")


abrir_arquivo()
