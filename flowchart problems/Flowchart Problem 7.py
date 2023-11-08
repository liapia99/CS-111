"""
File: Flowchart Problem 7
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 7

"""

ans = 'Y'

while ans == 'Y' or ans =='y':
    
    rp = int(input("What is your rate of pay?"))
    hw = int(input("How many hours did you work?"))
    tr = int(input("What is your tax rate?"))
    idn = int(input("What is your ID number?"))

    if hw > 40:
        ot = (hw - 40)*(rp * 1.5)
    else:
        ot = 0

    #endif

    gp = ( rp * 40 ) + ot

    to = ( gp * (tr/100) )

    np = ( gp - to )

    print("Your net pay is:", np, ".")
    print("Your gross pay is:", gp, ".")
    print("Your taxes owned is:", to, ".")
    print("Your ID is:", idn, ".")

    ans = input("Do again? (Y/N)")


print("End of Program.")



