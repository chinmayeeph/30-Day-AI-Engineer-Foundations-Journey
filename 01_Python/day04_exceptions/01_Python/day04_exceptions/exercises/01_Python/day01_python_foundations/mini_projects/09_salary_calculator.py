basic_salary = float(input("Enter your basic salary($): "))
appraisal_amount = float(input("Enter your appraisal_amount($): "))
tax_rate = 16

percentage_of_appraisal = (basic_salary / appraisal_amount) * 100
gross_salary = basic_salary + appraisal_amount
tax = (gross_salary*tax_rate) / 100
net_salary = gross_salary - tax

print(f"Congrajulations you have been hiked with {percentage_of_appraisal:.2f}% of Amount")
print(f"Your Gross Salary is {gross_salary:.2f}")
print(f"And based on current year Tax Rate {tax_rate}, the Tax deducted is {tax}")
print(f"Overall your Net Salary is {net_salary:.2f}")