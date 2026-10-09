# Returns the square
def calculate_square(n):
    return n * n

def main():
    number = int(input("Enter the number: "))
    print(calculate_square(number))

if __name__ == "__main__":
    main()



# Returns the cube
def calculate_cube(n):
    return n * n * n

def main():
    number = int(input("Enter the number: "))
    print(calculate_cube(number))

if __name__ == "__main__":
    main()



# Returns addition
def addition(a, b):
    return a + b

def main():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    print(addition(a, b))

if __name__ == "__main__":
    main()




# Returns average
def average(a, b, c):
    return (a + b + c) / 2

def main():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))
    print(average(a, b, c))

if __name__ == "__main__":
    main()




# Returns Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def main():
    celsius = float(input("Enter the number: "))
    print(celsius_to_fahrenheit(celsius))

if __name__ == "__main__":
    main()




# Returns BMI
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def main():
    weight_kg = int(input("Enter the weight in kgs: "))
    height_m = float(input("Enter the height in m: "))
    bmi = calculate_bmi(weight_kg, height_m)
    print(f"According to your weight and height, your BMI is {bmi:.2f}")

if __name__ == "__main__":
    main()





# Returns simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def main():
    principal = float(input("Enter the amount($): "))       # Principal Amount
    rate = float(input("Enter the rate(%): "))         # Annual Interest Percentage Rate 
    time = int(input("Enter the time(years): "))       # The Duration of the Loan or Investment in Years
    simple_interest = calculate_simple_interest(principal, rate, time)
    print(f"Your simple interest is {simple_interest:.2f}")

if __name__ == "__main__":
    main()




# Returns percentage
def calculate_percentage(marks_obtained, total_marks):
    return marks_obtained / total_marks * 100

def main():
    marks_obtained  = int(input("Enter the marks obtained by the student: "))
    total_marks  = 600
    percentage_of_student = calculate_percentage(marks_obtained, total_marks)
    print(f"Student's total percentage is {percentage_of_student:.2f}")

if __name__ == "__main__":
    main()