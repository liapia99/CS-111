"""
File: Flowchart Program 11
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 11

"""

x = input("Input a number ==>")

c = 1
max = x
    
if x == '-1':
    print("List is null and no max .")
else:
    while True:
        x = input("Input a number ==>")
        if x == '-1':
            break
            print("Max=",max,"Count=",c)
        else: 
            if x < max:
                
                c = c + 1
            else:
                max = x
                c = c + 1
                    
            #endif
        #endif  
#endif

print("Max=",max,"Count=",c)
print("End of Program.")
