number = int(input("Enter a number: "))

total = 0
temp = number

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("The sum of digits is:", total)