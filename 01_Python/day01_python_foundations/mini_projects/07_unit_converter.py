print("------Distance Converter------")
kilometers = float(input("Enter the number of kilometer: "))
miles = float(input("Enter the num,ber of meters: "))
kilometers = 0.621371 * kilometers
miles = 0.000621371 * miles
print(f"{kilometers} kilometers is equal to {miles} miles.")
print(f"{miles} miles is equal to {kilometers} kilometers.")

print("------Weight Converter------")
kilograms = float(input("Enter the weight in kilograms: "))
pounds = float(input("Enter the weight in pounds: "))
kilograms = pounds / 2.20462
pounds = kilograms * 2.20462
print(f"{kilograms} kilograms is equal to {pounds} pounds.")
print(f"{pounds} pounds is equal to {kilograms} kilograms.")