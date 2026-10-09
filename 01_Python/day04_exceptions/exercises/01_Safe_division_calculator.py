def main():
    x = get_int("What's the numerator?: ")
    y = get_int("What's the denominator: ")
    print(f" {x} / {y} is {x / y}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not an integer. Please try again.")
        except ZeroDivisionError:
            print("The denominator cannot be zero. Please try again.")
        else:
            pass

main()
            