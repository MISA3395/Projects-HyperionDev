# The following programme calculates the amount of interest the user will earn on their investment (investment) or,
# the amount they will have to pay on a home loan (bond). 
# They can choose the calculation either "investment" or "bond" which they want to do.
# The program will check either "investment" or "bond" entered by the user and then either of the following if-elif 
# statements will be executed.
# For investment, they can choose how to calculate using either "simple" or "compound" calculation methods.


import math # This is written in order to use math pow in the first elif-statement below.

# Output description of the calculation methods below.
investment_description = "investment - to calculate the amount of interest you'll earn on your investment"
bond_description = "bond - to calculate the amount you'll have to pay on a home loan\n"
print(investment_description)
print(bond_description)

# Ask the user to enter which calculation they want to do.
calculation = input("Please enter either 'investment' or 'bond' :  ") 

print("\n", end="") # make a white space. 

# If the user chose investment, the following if statement will be executed and the user can enter a number to calculate the investment.
if calculation.lower() == "investment" :
        deposit = int(input("Please enter how much you are depositing :  ")) 
        interest_rate = int(input("Please enter the interest rate :  "))  
        years_investing = int(input("Please enter how many years you plan on investing :  "))    

        print("\n", end="") # make a white space.

        # Users who choose investment can choose either "simple" or "compound" calculation methods.
        interest = input("Please enter the calculation method either 'simple' or 'compound' :  ") 
        
        print("\n", end="") # make a white space.

        # If the user chose simple, the following if statement will be executed. Also, calculate and output the result.
        if interest.lower() == "simple" :   
                # Calculation of the simple of investment.
                simple_calculation = deposit * ( 1 + interest_rate/100 * years_investing)  
                simple_result = round(simple_calculation)   
                simple_output = f"You will get back {simple_result}."
                print(simple_output)

        # If the user chose compound, the following elif statement will be executed. Also, calculate and output the result.   
        elif interest.lower() == "compound" :  
                # Calculation of the compound of investment.
                compound_calculation = deposit * math.pow(( 1 + interest_rate/100), years_investing)    
                compound_result = round(compound_calculation)     
                compound_output = f"You will get back {compound_result}."
                print(compound_output)

        # If the user entered an invalid character, the following else statement will be executed.
        else :
                print("You have entered an invalid character. Please enter either 'simple' or 'compound'.")

# If the user chose bond, the following elif statement will be executed and the user can enter a number to calculate the bond.
elif calculation.lower() == "bond" :   
        house_value = int(input("Please enter the present value of the house :  "))  
        interest_rate1 = int(input("Please enter the interest rate. :  "))  
        month_repay = int(input("Please enter how many months you plan to take to repay the bond? :  "))    

        print("\n", end="") # make a white space.

        # Calculation of bond.
        monthly_interest = interest_rate1 / 100  
        repayment_calculation = ((monthly_interest/12) * house_value)/(1 - (1 + monthly_interest/12)**(-month_repay)) 
        repayment_result = round(repayment_calculation)  
        repayment_output = f"You will have to repay {repayment_result} each month."
        print(repayment_output)

# If the user entered an invalid character, the following else statement will be executed.
else :
   print("You have entered an invalid character. Please enter either 'investment' or 'bond'")
