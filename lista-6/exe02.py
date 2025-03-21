from itertools import count

numbers = ()

for i in range(4):
    number = int(input("Expresse 4 Números Inteiros: "))
    numbers = numbers + (number,)

count_number_nine = numbers.count(9)
pos_number_three = numbers.index(3)

even_numbers = [num for num in numbers if num % 2 == 0]

print(f"O número 9 apareceu {count_number_nine} vezes.")
if pos_number_three != -1:
    print(f"O número 3 apareceu pela primeira vez na posição {pos_number_three}.")
print(f"Números pares contidos na tupla: {even_numbers}")