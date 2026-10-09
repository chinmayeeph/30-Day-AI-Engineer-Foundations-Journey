# Vanity Plates
# CS50 license plate
# 
# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
# 
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
# 
# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")
# 
# 
# def is_valid(s):
#     ...
# 
# 
# main()
# 
# 
# Hints
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Much like a list, a str is a “sequence” (of characters), which means it can be “sliced” into shorter strings with syntax like s[i:j]. For instance, if s is "CS50", then s[0:2] would be "CS".



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1. Check length (Must be between 2 and 6 characters)
    if not (2 <= len(s) <= 6):
        return False

    # 2. Check start (First two characters must be letters)
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # 3. Check punctuation (Must only contain letters and numbers)
    if not s.isalnum():
        return False

    # 4. Check number rules (No numbers in the middle, first number can't be '0')
    for i in range(len(s)):
        if s[i].isdigit():
            # If the first number found is '0', it's invalid
            if s[i] == '0':
                return False
            
            # Slice the remaining part of the plate. It MUST all be numbers.
            # If there is a letter after this point, .isdigit() will be False.
            if not s[i:].isdigit():
                return False
                
            # Once we successfully check the number portion, we can stop the loop
            break

    # If it survived all the checks above, it is valid!
    return True


if __name__ == "__main__":
    main()
