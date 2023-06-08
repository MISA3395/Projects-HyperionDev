# The following program is a simple calculator using a while repetition and defensive programming. 
# The user can input numbers and an operator they want to calculate.
# The user can choose to continue the calculation or see all equations and results from a text file.


while True :
    try:
        # Input numbers and an operator with the inputs below.
        num1 = int(input("\nPlease enter first Number: "))
        num2 = int(input('Please enter second number: '))
        operator = input("Please enter operation (+, -, * or / ): ") 
        print("\n", end="")
        
        if operator == "+" :
            equation = (num1 + num2)
            result = f"{num1} + {num2} = {equation}"

        elif operator == "-":
            equation = (num1 - num2)
            result = f"{num1} - {num2} = {equation}"
    
        elif operator == "*":
            equation = (num1 * num2)
            result = f"{num1} * {num2} = {equation}"
    
        elif operator == "/":
            equation = (num1 / num2)
            result = f"{num1} / {num2} = {equation}"

        # If the user entered an invalid operator, the following else statement will be executed.  
        else:
            print("You have entered an invalid operator. Please enter +, -, * or /.") 
        
        # Open a text file and all equations are written to the text file when the user enters a valid operator.
        if operator == "+" or operator == "-" or operator == "*" or operator == "/" :
            with open("all_equation.txt", "a") as file: 
                    file.write(result)
                    file.write("\n")
                    print(result)

            while True :    
                    print("\nYou have following two choices : ")
                    print("Calculate more - Please enter 'A'.")
                    print("Read all the calculated equations - Please enter 'B'.")

                    # Choose either choice A or B.
                    choice = input("\nPlease enter either 'A' or 'B' : ")

                    # If A was chosen, the calculation will be continued.
                    if choice.lower() == 'a' :
                       break

                    # If the user chose 'B', the following elif statement will be executed.
                    elif choice.lower() == "b" :
                        while True:
                            try:
                                # Input a file name and read them.
                                file_name = input("\nPlease enter the text file name : ")
                                with open(f'{file_name}.txt') as f:
                                    lines = f.read()
                                    print(lines)
                                    exit()
        
                            # If the file is not found, the except below will be executed.
                            except FileNotFoundError:
                                print(f"\nFile {file_name}.txt not found. Please enter a valid file name.")
            
                    # If the user entered except 'A' or 'B', the following else statement will be executed.
                    else :
                        print("\nYou have entered an invalid character. Please enter either 'A' or 'B'.")

    # If the user hasn't entered a number, the except below will be executed.
    except ValueError: 
        print("\nYou have entered an invalid character. Please enter a number.")

    # If the user tries to divide by zero, the except below will be executed.
    except ZeroDivisionError:   
        print("Can't divide by zero. Please enter except 0.")

