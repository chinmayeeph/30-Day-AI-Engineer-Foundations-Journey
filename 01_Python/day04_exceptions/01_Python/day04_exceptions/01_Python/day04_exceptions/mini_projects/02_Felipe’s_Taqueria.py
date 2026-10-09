def main():
    # The given menu dictionary with items and their prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    total_cost = 0.0

    while True:
        try:
            # Prompt the user for an item
            item = input("Item: ")
            
            # Convert to title case to match the dictionary keys case-insensitively
            item_title = item.title()
            
            # Check if the item exists in the menu
            if item_title in menu:
                total_cost += menu[item_title]
                # Print the total formatted to two decimal places
                print(f"Total: ${total_cost:.2f}")
                
        except EOFError:
            # Print a new line to keep the terminal clean and exit the loop
            print()
            break

if __name__ == "__main__":
    main()
