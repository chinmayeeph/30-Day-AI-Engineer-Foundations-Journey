num = int(input("Enter the number:"))

# Removed the unused input line since the loop handles the numbers 1-100

for num in range(1, 101):
    # 1. Check common multiples first
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZBUZZ")
    # 2. Check individual conditions next
    elif num % 3 == 0:
        print("FIZZ")
    elif num % 5 == 0:
        print("BUZZ")
    # 3. Print the actual number if none of the above match
    else:
        print(num)