age = int(input("Enter the age: "))

match age:
    case _ if 0 <= age <= 12:
        print("Category: Child")
    case _ if 13 <= age <= 17:
        print("Category: Teenager")
    case _ if 18 <= age <= 59:
        print("Category: Adult")
    case _ if age >= 60:
        print("Category: Senior")
    