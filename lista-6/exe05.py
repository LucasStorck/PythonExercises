clubs = (
    "Bahia", "Atlético-MG", "Botafogo", "Corinthians", "Fortaleza", "Cruzeiro", "Flamengo", "Fluminense",
    "Internacional",
    "Grêmio")

number = int(input("Digite um para de 1 a 10 para escolher um time: "))

if 1 <= number <= 10:
    club = clubs[number - 1]
    print(f"Com base no número digitado o timo escolhido foi: {club}")

for pos_start in clubs[:3]:
    print(f"Os Três Primeiros Clubes: {pos_start}")

for pos_end in clubs[-3:]:
    print(f"Os Três Últimos Clubes: {pos_end}")

order = sorted(clubs)

print(f"Em ordem Alfabética: {order}")
