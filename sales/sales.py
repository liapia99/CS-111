#########################################################
# Sales Commission Report using file : sales.dat
# File:  sales.py
# Author: Julia Piascik
# Date: Oct 24, 2022
#########################################################

salesfile = open( "sales.dat", mode = 'r' )

attendants = []                   # attendants null list
tcs = 0                         # total customers counter
tg = 0                         # total gallons sold accumulator
tco = 0.0                       # total commissions accumulator

#print headers
print("\n=============================================================")
print("                                       SALES COMMISSION")
print("")
print("     NAME              LOCATION               SOLD            COMMISSION")
print("===============================================================")
for attendant in salesfile:
              attendant = attendant.split()
              name = attendant[0]
              location = attendant[1]
              sold = int(attendant[2])
              if sold >500:
                            due = sold * 0.04
              else:
                            due = sold * 0.03
              #endif
              # accumulate and count
              tcs = tcs + 1
              tg = tg + sold
              tco = tco + due
              #output
              #print(name,title,sold,due)
              print( "%10s %19s %19i %18.2f"  %  (name,location,sold,due))
#end for
salesfile.close()
print("==============================================================")
print("  Total number of attendants   ==> ", tcs)
print("  Total gallons sold               ==> ",tg)
print("  Total commission           ==> $", round(tco,2))
print("\n .... End of job!")
salesfile.close()
# end of main
