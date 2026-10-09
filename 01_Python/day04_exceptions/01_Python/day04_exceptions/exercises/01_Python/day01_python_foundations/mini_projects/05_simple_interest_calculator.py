P = float(input("Enter the amount($): "))       # Principal Amount
R = float(input("Enter the rate(%): "))         # Annual Interest Percentage Rate 
T = int(input("Enter the time(years): "))       # The Duration of the Loan or Investment in Years
SI = (P * R * T)/100                            # Simple Interest Formula

print(f"Your simple interest is {SI:.2f}")