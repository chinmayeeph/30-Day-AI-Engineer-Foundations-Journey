def main():
    # The given list of months to validate and convert word-based months
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Date: ").strip()

        # Scenario 1: MM/DD/YYYY format
        if "/" in date_str:
            try:
                # Split by forward slashes
                month_str, day_str, year_str = date_str.split("/")
                
                # Convert to integers
                month = int(month_str)
                day = int(day_str)
                year = int(year_str)
                
                # Validate month and day boundaries
                if 1 <= month <= 12 and 1 <= day <= 31:
                    break
            except ValueError:
                # Catch cases with unexpected letters or improper spacing
                pass

        # Scenario 2: Month DD, YYYY format
        elif "," in date_str:
            try:
                # Split the string at the comma to isolate the year
                month_day, year_str = date_str.split(",")
                year = int(year_str.strip())
                
                # Split the remaining part by space to get month name and day
                month_name, day_str = month_day.strip().split(" ")
                day = int(day_str)
                
                # Look up the month name in our list (case-insensitive title match)
                month_name_title = month_name.title()
                if month_name_title in months:
                    # Index is 0-based, so add 1 to get the correct month integer
                    month = months.index(month_name_title) + 1
                    
                    # Validate day boundaries
                    if 1 <= day <= 31:
                        break
            except ValueError:
                pass

        # If it doesn't match either required format structure, the loop continues

    # Print the date formatted as YYYY-MM-DD with zero-padding
    print(f"{year}-{month:02}-{day:02}")

if __name__ == "__main__":
    main()
