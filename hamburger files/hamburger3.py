##########################
# File: hamburger3.py
# Author: Julia Piascik
# Date: Septemeber 4, 2022
##########################

# prices of burgers

priceBigHugo = 3
priceDoubCheese = 2
priceCheese = 1

#input order and amount received from customber into string variables

noBigHugo = input("\n Enter amount of Big Hugo burgers desired ==>")
noDoubCheese = input("\n Enter amount of Double Cheese burgers desired ==>")
noCheese = input("\n Enter amount of Cheese burgers desired ==>")
amtGiven = input("\n Enter dollar amount given by customer ==>$")

#calc cost burgers, converting string variable amounts into numeric values

costBigHugo = int(noBigHugo) * priceBigHugo
costDoubCheese = int(noDoubCheese) * priceDoubCheese
costCheese = int(noCheese) * priceCheese

# calc total cost of all burgers

total = costBigHugo + costDoubCheese + costCheese

# calc change converting string value of amtGiven into an integer value

change = int(amtGiven) - total

# output cost and change

print("\n The total cost of these burgers is $", total)
print("Your change from", amtGiven, "dollars is $", change)
print("\t Thank you!!! Come Again!")

# end program

