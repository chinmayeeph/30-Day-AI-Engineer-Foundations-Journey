# Day 3 — Loops

## Topics
* **for** loops
* **while** loops
* **range()** function
* **break** statement
* **continue** statement

## Mental Models
* **Repeat known sequence** → Use a `for` loop
* **Repeat while condition is true** → Use a `while` loop
* **Stop loop completely** → Use `break`
* **Skip current iteration** → Use `continue`

## Problems Completed
* Print 1–100
* Sum 1–100
* Factorial
* Multiplication table
* Countdown
* FizzBuzz
* Even numbers
* Odd numbers
* Count digits
* Reverse number
* Sum digits
* Prime checker
* Number guessing game
* Camel Case
* Coke Machine
* Just setting up my twttr
* Vanity Plates
* Nutrition Facts

## Challenge
* **Number Guessing Game** — Implementing a user-input loop that validates hot/low/correct responses dynamically.

## Biggest Difficulty
* **State Management & String Manipulation:** Shifting between updating state variables (like math totals for digit counting) and parsing strings character-by-character (like stripping vowels in `twttr` or validating `Vanity Plates`). 
* **Loop Control:** Knowing exactly when to trigger a `break` vs. a `continue` to avoid infinite loops, especially when managing remaining balances in the `Coke Machine`.

## What I Learned
* **Input Validation:** How to pair `while True` with `try/except` or conditional statements to build resilient code that doesn't crash on bad user input.
* **The Power of `range()`:** Step values can easily handle counting backward (countdowns) or skipping steps (even/odd numbers).
* **Text Processing:** Loops aren't just for math; iterating over strings allows you to filter, transform, and analyze text instantly.

## My Key Takeaway
> "I need to repeat something → think LOOP."