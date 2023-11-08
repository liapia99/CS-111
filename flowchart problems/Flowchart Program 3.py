"""
File: Flowchart Program 3
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 3

"""

B1 = 5000
B2 = 6000
B3 = 5500
W1 = 820
W2 = 910
W3 = 850

E1 = B1/W1
E2 = B2/W2
E3 = B3/W3

print(E1, E2, E3)

if E1 > E2 and E1 > E3:
    print("Buy Model A.")
else:
    if E2 > E1 and E2 > E3:
        print("Buy Model B.")
    else:
        print("Buy Model C.")

    #endif
#endif
        
print(" End of Program.")
