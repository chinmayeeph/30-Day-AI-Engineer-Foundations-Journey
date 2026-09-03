age = "25"              #since there is double quotes, it is considered as string. To convert it into integer, we can use int() function.
age = int(age)
print(age)
print(type(age))        #type is used to check the data type of the variable. In this case, it will print <class 'int'> since we converted the string to an integer.

price = 99
price = float(price)    #since there is no decimal point, it is considered as integer. To convert it into float, we can use float() function.
print(price)
print(type(price))      #type is used to check the data type of the variable. In this case, it will print <class 'float'> since we converted the integer to a float.

number = 100
text = str(number)      #since there is no double quotes, it is considered as integer. To convert it into string, we can use str() function.
print(text)
print(type(text))       #type is used to check the data type of the variable. In this case, it will print <class 'str'> since we converted the integer to a string.