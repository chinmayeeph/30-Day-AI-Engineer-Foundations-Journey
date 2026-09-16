Product_price = float(input("Enter the price of product($): "))
Quantity = int(input("Enter the quantity: "))
subtotal = Product_price*Quantity
discount_percentage = float(input("Enter the percentage of discount for the product(%): "))
discount = subtotal*discount_percentage / 100
final_price = subtotal - discount

print(f"Total bill is {final_price:.2f}")