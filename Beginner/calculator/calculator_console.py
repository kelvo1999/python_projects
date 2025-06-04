# This calculator is used mainly on the console for basic arithmetics


def console_calculator():
    print("Simple Console Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Modulus (%)")
    print("5. Division (/)")
    print("6. Exit")
    
    while True:
        try:
            choice = input("Enter operation (1/2/3/4/5/6): ")
            
            if choice == '5':
                print("Exiting calculator...")
                break
                
            if choice not in ('1', '2', '3', '4','5'):
                print("Invalid input. Please try again.")
                continue
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif choice == '5':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                    
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the console calculator
console_calculator()
