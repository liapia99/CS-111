#Program to count how many customers bought vanilla and chocolate ice cream from a shop and state whether (by the end of the day), customers like vanilla better or chocolate. 
vp = 0
cp = 0

while True:
    
    idn = input("Customer Number: ")
    if idn != '-999':

        v = int(input("How many vanilla ice creams were bought?"))
        c = int(input("How many chocolate ice creams were bought?"))

        if v == c:
            vp = vp + 0
            cp = cp + 0
            if cp == vp:
                cp = cp
                vp = vp
            else:
                if cp > vp:
                    d = ((cp-vp)/((cp + vp)/2))*100
                    print("Customers like chocolate better by: ",d,"%. Make more chocolate.")
                    
                else:
                    p = ((vp-cp)/((vp + cp)/2))*100
                    print("Customers like vanilla better by: ",p,"%. Make more vanilla.")
                    
                #endif
            #endif
        else:
            if v > c:
                vp = vp + 1
            else:
                cp = cp + 1
            #endif
        #endif
    else:
        
        break

    #endif
    print("Customers like chocolate better by: ",d,"%. ")
    print("Customers like vanilla better by: ",p,"%. ")

#end while
    


print("End.")

#end program
