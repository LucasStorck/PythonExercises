numbers = []
for i in range(1, 4):
    number = float(input("Enter a number: "))
    numbers.append(number)

def calculator():
    average = sum(numbers) / len(numbers)
    return average

print(f"The average of the numbers is: {calculator()}")
