"""
File: Flowchart Program 13
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 13

"""
x = float(input("Input a value for x ==>"))

while True:
    

    if x <= 0:
        x = float(input("Input a value for x ==>"))
    else:
        if x > 100:
            print("Value is too large.")
            break
        else:
            if x > 90:
                sum = 50 + 51 + 52 + 53 + ... + x
                print(sum)
                break
            else:
                sum = 1 + 2 + 3 + 4 + ... + x
                print(sum)
                break
            #endif
        #endif
    #endif
        
print("Goodbye.")
print("End of Program.")
