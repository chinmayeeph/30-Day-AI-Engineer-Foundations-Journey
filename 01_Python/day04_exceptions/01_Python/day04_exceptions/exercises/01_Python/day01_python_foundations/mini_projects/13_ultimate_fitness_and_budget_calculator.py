# --- 1. User Profile Setup (Strings & Variables) ---
print("-----WELCOME TO YOUR PERSONAL DASHBOARD-----")
user_name = input("Enter Your Name: ")

# --- 2. Input & Type Conversion (int, float) ---
weight_kg = float(input("Enter your weight in kg: "))
height_ft = float(input("Enter your height in ft: "))
monthly_budget = float(input("Enter your total monthly budget ($): "))
daily_expenses = float(input("Enter your estimated daily expenses ($): "))
is_member = input("Are you a premium member? (True/False): ")

# --- 3. Calculations (Arithmetic Operators) ---
# ADDED: Convert feet to meters (1 foot = 0.3048 meters)
height_m = height_ft * 0.3048
# Calculate BMI: weight / (height squared)
bmi = weight_kg / (height_m ** 2)

# Calculate monthly savings projections
monthly_expense = daily_expenses * 30
savings = monthly_budget - monthly_expense

# --- 4. Logic & Evaluations (Comparison & Logical Operators) ---
# A healthy BMI generally falls between 18.5 and 24.9
is_healthy_bmi = (bmi >= 18.5) and (bmi <= 24.9)

# Financial safety check: Saving money AND staying within budget
is_saving_money = savings > 0
is_financial_secure = is_saving_money and (monthly_expense <= monthly_budget)

# Exclusive benefits check
gets_discount = is_member or (savings > 500.0)

# --- 5. Display Results (print() & Type Conversion to str) ---
print("\n---PERFORMANCE SUMMARY FOR " + user_name.upper() + "---")
print("Your Calculated bmi: " + str(bmi))
print("Is your BMI in the standard healthy range? " + str(is_healthy_bmi))
print("Projected Monthly Savings: $" + str(savings))
print("Are you financially secure this month? " + str(is_financial_secure))
print("Eligible for premium tier perks? " + str(gets_discount))