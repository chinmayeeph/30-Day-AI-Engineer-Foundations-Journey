a = 34
b = 457

print("------- Arithmetic Operators -------")
print(a + b)  # addition operator #returns the value of a plus b
print(a - b)  # subtraction operator #returns the value of a minus b
print(a * b)  # multiplication operator #returns the value of a multiplied by b
print(a / b)  # division operator #returns the value of a divided by b
print(a % b)  # modulus operator #returns the remainder of a divided by b
print(a ** b) # exponentiation operator #returns the value of a raised to the power of b
print(a // b) # floor division operator #returns the integer value of a divided by b
print("------- Comparison Operators -------")
print(a == b) # equal to operator #returns true if a is equal to b otherwise returns false
print(a != b) # not equal to operator #returns true if a is not equal to b otherwise returns false
print(a < b)  # less than operator #returns true if a is less than b otherwise returns false
print(a > b)  # greater than operator #returns true if a is greater than b otherwise returns false
print(a <= b) # less than or equal to operator #returns true if a is less than or equal to b otherwise returns false
print(a >= b) # greater than or equal to operator #returns true if a is greater than or equal to b otherwise returns false
print("------- logical Operators -------")
print(a and b) # logical and operator  #returns true if both the conditions are true otherwise returns false
print(a or b)  # logical or operator #returns true if any of the conditions is true otherwise returns false
print(not a)   # logical not operator #returns true if the condition is false and returns false if the condition is true
print("------- Assignment Operators -------")
print(a += b) # add and assign operator #returns the value of a plus b and assigns the value to a
print(a -= b) # subtract and assign operator #returns the value of a minus b and assigns the value to a
print(a *= b) # multiply and assign operator #returns the value of a multiplied by b and assigns the value to a
print(a /= b) # divide and assign operator #returns the value of a divided by b and assigns the value to a
print(a %= b) # modulus and assign operator #returns the value of a divided by b and assigns the remainder to a
print(a **= b) # exponentiation and assign operator #returns the value of a raised to the power of b and assigns the value to a
print(a //= b) # floor division and assign operator #returns the value of a divided by b and assigns the integer value to a
print("------- Bitwise Operators -------")
print(a & b)  # bitwise and operator #returns 1 if both bits are 1 otherwise returns 0
print(a | b)  # bitwise or operator  #returns 1 if any of the bits is 1 otherwise returns 0
print(a ^ b)  # bitwise xor operator  #returns 1 if both bits are different otherwise returns 0
print(a ~ b)  # bitwise not operator  #returns 1 if both bits are different otherwise returns 0
print(a << b) # bitwise left shift operator  #returns the value of a shifted left by b bits
print(a >> b) # bitwise right shift operator  #returns the value of a shifted right by b bits
print(a &= b) # bitwise and assign operator  #returns 1 if both bits are 1 otherwise returns 0
print(a |= b) # bitwise or assign operator  #returns 1 if any of the bits is 1 otherwise returns 0
print(a ^= b) # bitwise xor assign operator  #returns 1 if both bits are different otherwise returns 0
print(a <<= b) # bitwise left shift assign operator  #returns the value of a shifted left by b bits
print(a >>= b) # bitwise right shift assign operator  #returns the value of a shifted right by b bits
print("------- Membership Operators -------")
print(a in b)    # membership operator  #returns true if a is present in b
print(a not in b) # membership operator  #returns true if a is not present in b
print("------- Identity Operators -------")
print(a is b)    # identity operator  #returns true if both variables are the same object
print(a is not b) # identity operator  #returns true if both variables are not the same object
print("------- Ternary Operators -------")
print("Value of a is greater than b" if a > b else "Value of b is greater than a")  #here first condition is checked if it is true then first statement is executed otherwise second statement is executed
