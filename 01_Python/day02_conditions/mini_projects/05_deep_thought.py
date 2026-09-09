def main():
    # Prompt the user for input and clean it up immediately
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    # Check the input using match-case
    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":
    main()