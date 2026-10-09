def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("what is x?: "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()



# or

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("what is x?: "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()



# or

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("what is x?: "))
            return x
        except ValueError:
            print("x is not an integer")      

main()



# or

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("what is x?: "))
        except ValueError:
            print("x is not an integer")      

main()

