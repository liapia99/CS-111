##########################
# File: hamburger2.py
# Author: Julia Piascik
# Date: Septemeber 4, 2022
##########################

# cost of burgers

priceBigHugo = 3
priceDoubCheese = 2
priceCheese = 1  
# calc cost of burgers
costBigHugo = 2 * priceBigHugo
costDoubCheese = 2 * priceDoubCheese
costCheese = 2 * priceCheese

# calc total cost of all burgers
total = costBigHugo + costDoubCheese + costCheese

# calc change from $20
change = 20 - total

#output cost and change
print("\n The total cost of these burgers is $",total)
print("Your change from 20 dollars is $", change)
print("\tThank you!!! Come Again!")

#end program
