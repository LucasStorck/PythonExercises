age = int(input("What is your age?: "))

if age < 18:
    print("You are a minor")
elif 18 >= age <= 59:
    print("You are an adult")
else:
    print("You are an elderly person")