def main():
    grocery_list = {}

    while True:
        try:
            # Prompt the user for an item and strip whitespace
            item = input().strip().upper()
            
            # If the item is already in our dictionary, increment its count
            if item in grocery_list:
                grocery_list[item] += 1
            # Otherwise, initialize its count to 1
            else:
                grocery_list[item] = 1
                
        except EOFError:
            # Print a blank line to clear the prompt line
            print()
            
            # Sort the dictionary keys alphabetically and print the results
            for sorted_item in sorted(grocery_list.keys()):
                print(f"{grocery_list[sorted_item]} {sorted_item}")
            
            # Exit the loop and end the program
            break

if __name__ == "__main__":
    main()
