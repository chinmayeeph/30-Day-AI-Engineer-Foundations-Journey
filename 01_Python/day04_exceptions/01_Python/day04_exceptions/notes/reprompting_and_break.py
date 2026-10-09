while True:       # if u type other than integer, the while loop helps u to tell again what is x
    try:
        x = int(input("what is x?: "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")