def main():
    x = get_valid_integer("Please enter an integer: ")
    print(f"Accepted number: {x}")

def get_valid_integer(prompt):
    while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please try again.")
            else:
                break

main()