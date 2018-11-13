number = int(input("Please choose a number: "))
if number % 4 == 0:
    print(f"{number} is even and is divisible by 4!")
elif number % 2 == 0:
    print(f"{number} is an even number!")
else:
    print(f"{number} is an odd number!")

check = int(input("Please choose another number: "))
if number % check == 0:
    print(f"{number} is divisible by {check}!")
else:
    print(f"{number} is not divisible by {check}!")
