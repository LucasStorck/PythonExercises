phrase = input("Expresse uma frase: ")

word_count = {}

words = phrase.split()

for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
print("Contagem de Caracteres: ", word_count)