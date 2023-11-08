"""
File: Flowchart Program 8
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 8

"""
ans = 'Y'

while ans == 'Y' or ans =='y':
    
    base = 185.00

    idn = input("What is your ID number?")
    wsales = float(input("What are your weekly sales?"))

    if wsales > 1000.00:
        if wsales > 5000.00:
            wpay = ((5000.00 - wsales) * (0.078)) + base + (5000.00 * 0.053)
        else:
            wpay = base + (wsales * 0.053)
    else:
        wpay = base
        #endif
    #endif
        
    print("Your ID number is:", idn,".")
    print("Your weekly sales are:",wsales,".")
    print("Your weekly pay is:", wpay,".")

    ans = input("Do again? (Y/N)")
    
    


print("End of Program.")

==== RESTART: /Users/juliapiascik/Documents/CS 111-B/flowchart-problem-8.py ====
What is your ID number? 101
What are your weekly sales? 955.00
Your ID number is:  101 .
Your weekly sales are: 955.0 .
Your weekly pay is: 185.0 .
Do again? (Y/N)Y
What is your ID number? 102
What are your weekly sales? 2000.00
Your ID number is:  102 .
Your weekly sales are: 2000.0 .
Your weekly pay is: 291.0 .
Do again? (Y/N)Y
What is your ID number? 103
What are your weekly sales? 6000.00
Your ID number is:  103 .
Your weekly sales are: 6000.0 .
Your weekly pay is: 372.0 .
Do again? (Y/N)n
End of Program.
