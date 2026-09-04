a = 10
b = 5

print("------- Arithmetic Operators -------")
print(a + b)  # addition operator #returns the value of a plus b 
# outputs -> 15
print(a - b)  # subtraction operator #returns the value of a minus b
# outputs -> 5
print(a * b)  # multiplication operator #returns the value of a multiplied by b
# outputs -> 50
print(a / b)  # division operator #returns the value of a divided by b
# outputs -> 2.0
print(a % b)  # modulus operator #returns the remainder of a divided by b
# outputs -> 0
print(a ** b) # exponentiation operator #returns the value of a raised to the power of b
# outputs -> 100000
print(a // b) # floor division operator #returns the integer value of a divided by b
# outputs -> 2

print("------- Comparison Operators -------")
print(a == b) # equal to operator #returns true if a is equal to b otherwise returns false
# outputs -> False
print(a != b) # not equal to operator #returns true if a is not equal to b otherwise returns false
# outputs -> True
print(a < b)  # less than operator #returns true if a is less than b otherwise returns false
# outputs -> True
print(a > b)  # greater than operator #returns true if a is greater than b otherwise returns false
# outputs -> False
print(a <= b) # less than or equal to operator #returns true if a is less than or equal to b otherwise returns false
# outputs -> True
print(a >= b) # greater than or equal to operator #returns true if a is greater than or equal to b otherwise returns false
# outputs -> False

print("------- logical Operators -------")
print(a and b) # logical and operator  #returns true if both the conditions are true otherwise returns false
# outputs -> 5
print(a or b)  # logical or operator #returns true if any of the conditions is true otherwise returns false
# outputs -> 10
print(not a)   # logical not operator #returns true if the condition is false and returns false if the condition is true
# outputs -> False

print("------- Assignment Operators -------")
a += b        # add and assign operator: returns the value of a plus b and assigns it to a
print(a)         # outputs -> 15
a -= b        # subtract and assign operator: returns the value of a minus b and assigns it to a
print(a)         # outputs -> 10
a *= b        # multiply and assign operator: returns the value of a multiplied by b and assigns it to a
print(a)         # outputs -> 50
a /= b        # divide and assign operator: returns the value of a divided by b and assigns it to a
print(a)         # outputs -> 10.0
a %= b        # modulus and assign operator: returns the remainder of a divided by b and assigns it to a
print(a)         # outputs -> 0.0
a **= b       # exponentiation and assign operator: returns the value of a raised to the power of b and assigns it to a
print(a)         # outputs -> 0.0
a //= b       # floor division and assign operator: returns the integer value of a divided by b and assigns it to a
print(a)         # outputs -> 0.0

print("------- Bitwise Operators -------")
a &= b       # bitwise and assign operator  #returns 1 if both bits are 1 otherwise returns 0
print(a)         # outputs -> 0     
a |= b       # bitwise or assign operator  #returns 1 if any of the bits is 1 otherwise returns 0
print(a)         # outputs -> 5
a ^= b       # bitwise xor assign operator  #returns 1 if both bits are different otherwise returns 0
print(a)         # outputs -> 0
a <<= b      # bitwise left shift assign operator  #returns the value of a shifted left by b bits
print(a)         # outputs -> 0
a >>= b      # bitwise right shift assign operator  #returns the value of a shifted right by b bits
print(a)         # outputs -> 0

print("------- Membership Operators -------")
a = 10
b = [5, 10, 15, 20]
print(a in b)      # membership operator  #returns true if a is present in b
# outputs -> True
print(a not in b)  # membership operator  #returns true if a is not present in b
# outputs -> False

print("------- Identity Operators -------")
print(a is b)      # identity operator  #returns true if both variables are the same object
# outputs -> False
print(a is not b)  # identity operator  #returns true if both variables are not the same object
# outputs -> True

print("------- Ternary Operators -------")
print("Value of a is greater than b" if a > b else "Value of b is greater than a")  # here first condition is checked if it is true then first statement is executed otherwise second statement is executed
# outputs -> Value of a is greater than b