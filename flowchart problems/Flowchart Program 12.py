"""
File: Flowchart Program 12
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 12

"""
xgy = 0
xly = 0

while True:
    x = input("Input a value for x ==>")
    y = input("Input a value for y ==>")


    if x == y:
        break
    else:
        if x > y:
            xgy = xgy + 1
        else:
            xly = xly + 1
        #endif
    #endif

print("Pairs that satisfy x < y :",xly,"Pairs that satisfy x > y : ",xgy)
print("End of Program.")
