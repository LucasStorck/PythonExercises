word = input("Expresse uma palavra: ")

char_count = {}

for char in word:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1
print("Contagem de Caracteres: ", char_count)