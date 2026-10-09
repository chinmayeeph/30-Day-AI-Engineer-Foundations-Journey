try:
    x = int(input("what is x?: "))
except ValueError:
    print("x is not an integer")
else:                               # IF ELSE NOT MENTIONED IT WILL PROVIDE NameError
    print(f"x is {x}")