# Coke Machine
# CS50 Coke Bottle
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
# 
# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.





# Initialize the starting cost of the Coke
amount_due = 50

# Keep looping until the amount due is fully paid or exceeded
while amount_due > 0:
    # Print the current amount due
    print(f"Amount Due: {amount_due}")
    
    # Prompt the user to insert a coin
    coin = int(input("Insert Coin: "))
    
    # Validate the coin; only accept 25, 10, or 5 cents
    if coin in [25, 10, 5]:
        # Subtract the valid coin value from the amount due
        amount_due -= coin

# Once the loop ends, calculate and print the change owed (if any)
# Since amount_due can be negative, absolute value gives the positive change amount
print(f"Change Owed: {abs(amount_due)}")