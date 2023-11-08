"""
File: Flowchart Program 9
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 9

"""
    
X = int(input("Plug in a vlaue for x ==> "))

Z = int(input("Plug in a vlaue for z ==> "))

if X + Z == 42:
    print("42")
else:
    while True:
        X2 = X + 10
        Z2 = Z + 3
        print(X2)
        print(Z2)
        if X2 + Z2 >= 42:
            print("42")
        else:
            X2 = X2 + 10
            Z2 = Z2 + 3
            print(X2)
            print(Z2)
            if X2 + Z2 >= 42:
                print("42")
                break
        #endif
#endif

print("End of Program.")
