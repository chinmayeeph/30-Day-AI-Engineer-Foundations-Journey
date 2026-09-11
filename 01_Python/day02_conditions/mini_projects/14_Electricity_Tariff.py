# input
units_str = input("How many units did you consume? ")

# conversion
units = float(units_str)

# if, elif, else logic to determine the rate
if units <= 100:
    rate = 50
elif units <= 200:
    rate = 70
elif units <= 300:
    rate = 100
else:
    rate = 120

# calculation
bill = units * rate

# output
print("\n========================================")
print("       ELECTRICITY BILL RECEIPT         ")
print("========================================")
print(f"Units: --------------------{int(units)}")
print(f"Rate: ---------------------₹{rate}/unit")
print("========================================")
print(f"Bill: ---------------------₹{int(bill)}")
print("========================================")