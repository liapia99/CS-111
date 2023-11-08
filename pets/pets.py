# using seq files and functions

def getPets():
    petL = []
    petsFile = open("pets.dat", 'r')
    for pet in petFile:
        pet = pet.split()
        petL.append(pet)
    # end for pet
    petFile.close()
    return petL
# end ftn getPets

def calcAveCost(allPets):
    sum = 0 #accumalator has to be before the loop
    c = 0
    for pet in allPets:
        c = c + 1
        cost = float(pet[4])
        sum = cost + sum 

    avg = sum /c
    return ave
def output (petName, cost):
    print("the average cost", petName, "is $",cost)
# main program- cna only pass whats under this point in the main 

allPets,c = getPets()

aveCost = calcAveCost(allPets)

    
