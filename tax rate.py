#program to get the tax rate of a purchase
def get():
    price = float(input("Enter the price:"))
    quantity = int(input("Enter the quantity:"))
    taxRate = float(input("Enter the tax rate:"))
    return price, quantity, taxRate
#end ftn get

def process(price, quantity, taxRate):
    salesAmt = price * quantity
    taxes = calcTax (salesAmt, taxRate)
    finalCost = (taxes + salesAmt ) 
    return finalCost
#end ftn process

def calcTax( salesAmt, taxRate):
    salesTax = salesAmt * taxRate
    return salesTax
#end ftn calcTax


def output(finalCost):
    print("the final cost is $", finalCost)
    return output
#end ftn output

# main program

price, quantity, taxRate = get()

finalCost = process(price, quantity, taxRate)

output(finalCost)


# end program
