hours = int(input("Enter the total hours worked in the month: "))
value = float(input("Enter the value of the hour worked: "))

def calculator():
    total_salary = hours * value
    return total_salary
print(f"Salary: {calculator()}")
