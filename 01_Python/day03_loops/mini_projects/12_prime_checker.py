number = int(input("Enter a number: "))

# Numbers less than or equal to 1 are not prime
if number <= 1:
    print(f"{number} is not prime")
else:
    is_prime = True

    # Check divisors from 2 up to (number - 1)
    for i in range(2, number):
        if number % i == 0:
            is_prime = False  # Found a divisor, so it's not prime
            break             # No need to check further, exit the loop

        # Print the final result after the loop finishes
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")