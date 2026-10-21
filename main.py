
# Python Basic Calculator

print("===== BASIC CALCULATOR =====")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulo (%)")

choice = input("Choose an operation (1-5): ")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    elif choice == "5":
        if num2 == 0:
            print("Error: Cannot use zero as the modulo divisor!")
        else:
            print("Result:", num1 % num2)

    else:
        print("Invalid choice. Please select 1-5.")

except ValueError:
    print("Error: Please enter valid numbers.")

Add basic Python calculator
