#Write a Python program to demonstrate handling multiple exceptions
def divide_numbers():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid integer numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print("Unexpected error occurred:", e)
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

divide_numbers()
