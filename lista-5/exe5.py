celsius = float(input("Expresse a temperatura em Celsius: "))


def conversor_temperatura(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


celsius_in_fahrenheit = conversor_temperatura(celsius)
print(f"A temperatura em Fahrenheit é {celsius_in_fahrenheit}")
