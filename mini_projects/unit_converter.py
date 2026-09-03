print("------Distance Converter------")
kilometers = float(input("Enter the number of kilometer: "))
miles = float(input("Enter the num,ber of meters: "))
kilometers = 0.621371 * kilometers
miles = 0.000621371 * miles
print(f"{kilometers} kilometers is equal to {miles} miles.")
print(f"{miles} miles is equal to {kilometers} kilometers.")

print("------Temperature Converter------")
celsius = float(input("Enter the temperature in celsius: "))
farenheit = float(input("Enter the temperature in farenheit: "))
celsius = farenheit * 9 / 5 + 32
farenheit = (celsius - 32) * 5 / 9
print(f"{celsius} celsius is equal to {farenheit} farenheit.")
print(f"{farenheit} farenheit is equal to {celsius} celsius.")

print("------Weight Converter------")
kilograms = float(input("Enter the weight in kilograms: "))
pounds = float(input("Enter the weight in pounds: "))
kilograms = pounds / 2.20462
pounds = kilograms * 2.20462
print(f"{kilograms} kilograms is equal to {pounds} pounds.")
print(f"{pounds} pounds is equal to {kilograms} kilograms.")