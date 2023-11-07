# program to determine the average age of a family ( or a group of people) and output how much younger or older someone is from that average group age
def getInfo():
    masterL = []
    classFile = open("file.dat", 'r')
    for stud in classFile:
        stud = stud.split()
        masterL.append(stud)
    #end for stud
    classFile.close()
    return masterL
# end ftn getInfo
def calcAvg(masterL):
    sum = 0
    c = 0
    for stud in masterL:
        sum = sum + int(stud[1])
        c = c + 1
    #end for stud
    avg = sum/c
    return avg
#end ftn calcAvg
def calcDev(masterL, avg):
    devL = []
    for stud in masterL:
        dev = int(stud[1])-avg
        studRecL = [stud[0], dev]
        devL.append(studRecL)
    #end for stud
    return devL
#end ftn calcDev


def outputDev(devL):
    for stud in devL:
        if stud[1]>0:
            print(stud[0],"is older by", stud[1], "from the average age.")
        else:
            print(stud[0],"is younger by", stud[1], "from the average age.")
        
    #end for stud
#end ftn outputDev

#main program
masterL = getInfo()
avg = calcAvg(masterL)
devL = calcDev(masterL, avg)
outputDev(devL)
#end main program

    
