# Problem - Indoor Voice
# WRITING IN ALL CAPS IS LIKE YELLING.
# Best to use your “indoor voice” sometimes, writing entirely in lowercase.
# In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

user_input = input("Enter the yelling: ").strip().lower()
print(user_input)

# In uppercase.
user_input = input("Enter the yelling: ").strip().upper()
print(user_input)

# Starting letters of a word in uppercase and est in lowercase.
user_input = input("Enter the yelling: ").strip().title()
print(user_input)