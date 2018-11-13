number = int(input("Enter a number: "))
divisors = []

for x in range(1, (number + 1)):
    if number % x == 0:
        divisors.append(x)
print(divisors)
