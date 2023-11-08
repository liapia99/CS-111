##########################
# File: hamburger4.py
# Author: Julia Piascik
# Date: Septemeber 4, 2022
##########################

# burgerm prices

priceBigHugo = 3.27
priceDoubCheese = 2.50
priceCheese = 1.55

# input order and amount received from customer

noBigHugo = input("\n Enter amount of Big Hugo burgers desired ==>")
noDoubCheese = input("\n Enter amount of Double Cheese burgers desired ==>")
noCheese = input("\n Enter amount of Cheese burgers desired ==>")
amtGiven = input("\n Enter dollar amount given by customer ==>$")

#calc cost burgers, converting string variable amounts into numeric values
#calc cost burgers, converting string variable amounts into numeric values

costBigHugo = float(noBigHugo) * priceBigHugo
costDoubCheese = float(noDoubCheese) * priceDoubCheese
costCheese = float(noCheese) * priceCheese

# calc total cost of all burgers

total = costBigHugo + costDoubCheese + costCheese

# calc change converting string value of amtGiven into an integer value

change = float(amtGiven) - total

# output cost and change

print("\n The total cost of these burgers is $", total)
print("Your change from", amtGiven, "dollars is $", change)
print("\t Thank you!!! Come Again!")

# end program
