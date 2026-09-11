# Problem - Home Federal Savings Bank

# In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.



# 1. Prompt the user for input and clean it right away
greeting = input("Greeting: ").strip().lower()

# 2. Use match-case to check patterns
match greeting:
    # Check if the string starts with "hello"
    case _ if greeting.startswith("hello"):
        print("$0")
        
    # Check if the string starts with "h" (but didn't match "hello")
    case _ if greeting.startswith("h"):
        print("$20")
        
    # Default case for anything else (wildcard)
    case _:
        print("$100")