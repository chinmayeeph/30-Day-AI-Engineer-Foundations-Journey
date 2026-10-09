amount = int(input("Amount($): "))

match amount:
    case _ if amount >= 5000:
        discount_rate = 0.20
    case _ if 3000 <= amount <= 4999:
        discount_rate = 0.10
    case _ if amount < 3000:
        discount_rate = 0.00

# 1. Calculate the dollar value of the discount
discount_money = amount * discount_rate

# 2. Subtract that dollar value from the total amount
final_amount = amount - discount_money

# 3. Print the results (using :.2f to show two decimal places for cents)
print(f"Discount: ${discount_money: }")
print(f"Final amount: ${final_amount: }")