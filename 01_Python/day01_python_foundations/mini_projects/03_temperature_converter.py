print("------Temperature Converter------")
celsius = float(input("Enter the temperature in celsius: "))
farenheit = float(input("Enter the temperature in farenheit: "))
celsius = farenheit * 9 / 5 + 32
farenheit = (celsius - 32) * 5 / 9
print(f"{celsius} celsius is equal to {farenheit} farenheit.")
print(f"{farenheit} farenheit is equal to {celsius} celsius.")