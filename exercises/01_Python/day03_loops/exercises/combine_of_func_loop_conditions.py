# Cat sounding meow!!

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            return n

def meow(number):
    for _ in range(number):
        print("Meow!")

main()