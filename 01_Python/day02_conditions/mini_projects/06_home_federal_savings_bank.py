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