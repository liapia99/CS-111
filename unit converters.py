#################################
# File: Unit Converter
# Name: Julia Piascik
# Date: Nov 12, 2022
#################################




def get():
    unitOne = str(input("Enter the unit you are starting with (IN for inches, CM for centimeters, FT for feet and M for meters:"))
    numOne = float(input("Enter the starting number:"))
    unitTwo = str(input("Enter the unit you want to end with (IN for inches, CM for centimeters, FT for feet and M for meters:"))
    return unitOne, numOne, unitTwo
#end ftn get

def intocm(numOne):
    inchangetocm = numOne * 2.54
    return inchangetocm
#end ftn intocm

def intoft(numOne):
    inchangetoft = numOne * 0.0833333
    return inchangetoft
#end ftn intoft

def intom(numOne):
    inchangetom = numOne * 0.0254
    return inchangetom
#end ftn intom

def cmtoin(numOne):
    cmchangetoin = numOne * 0.393701
    return cmchangetoin
#end ftn cmtoin

def cmtoft(numOne):
    cmchangetoft = numOne * 0.0328084
    return cmchangetoft
#end ftn cmtoft

def cmtom(numOne):
    cmchangetom = numOne * 0.01
    return cmchangetom
#end ftn cmtom

def fttoin(numOne):
    ftchangetoin = numOne * 12
    return ftchangetoin
#end ftn fttoin

def fttocm(numOne):
    ftchangetocm = numOne * 30.48
    return ftchangetocm
#end ftn fttocm

def fttom(numOne):
    ftchangetom = numOne * 0.3048
    return ftchangetom
#end ftn fttom

def mtoin(numOne):
    mchangetoin = numOne * 39.3701
    return mchangetoin
#end ftn mtoin

def mtocm(numOne):
    mchangetocm = numOne * 100
    return mchangetocm
#end ftn mtocm

def mtoft(numOne):
    mchangetoft = numOne * 3.28084
    return mchangetoft
#end ftn mtoft





#main program

print("Welcome to the unit converter!")
print("#################################################")
unitOne, numOne, unitTwo = get()

if unitOne == 'IN' or unitOne =='in':
    if unitTwo == 'CM' or unitTwo == 'cm':
        print(intocm(numOne),"CM")
    else:
        if unitTwo == 'FT' or unitTwo == 'ft':
            print(intoft(numOne),"FT")
        else:
            print(intom(numOne),"M")
            #endif
        #endif
    #endif
else:
    if unitOne == 'CM' or unitOne =='cm':
        if unitTwo == 'IN' or unitTwo == 'in':
            print(cmtoin(numOne),"IN")
        else:
            if unitTwo == 'FT' or unitTwo == 'ft':
                print(cmtoft(numOne),"FT")
            else:
                print(cmtom(numOne),"M")
            #endif
        #endif
    else:
        if unitOne == 'FT' or unitOne =='ft':
            if unitTwo == 'CM' or unitTwo == 'cm':
                print(fttocm(numOne),"CM")
            else:
                if unitTwo == 'IN' or unitTwo == 'in':
                    print(fttoin(numOne),"IN")
                else:
                    print(fttom(numOne),"M")
                #endif
            #endif
        else:
            if unitOne == 'M' or unitOne =='m':
                if unitTwo == 'CM' or unitTwo == 'cm':
                    print(mtocm(numOne),"CM")
                else:
                    if unitTwo == 'IN' or unitTwo == 'in':
                        print(mtoin(numOne),"IN")
                    else:
                        print(mtoft(numOne),"FT")
                #endif
            #endif
        #endif
    #endif
#endif 

#end of program
                

