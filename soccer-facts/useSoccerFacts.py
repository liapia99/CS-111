import createSoccerFacts
from createSoccerFacts             import lewFacts
from createSoccerFacts             import mbaFacts
from createSoccerFacts             import perFacts
from createSoccerFacts             import joFacts
from createSoccerFacts             import ricFacts

#   =============================================================================
#   File:  useClassSoccerFacts.py
#   Purpose: This is the main program that will use the class:soccerFacts that
#   contains soccer facts.
#   Name: Julia Piascik
#   =============================================================================

while True:
        print( "	     ================================================== ")
        print( "	        Choose a letter to see a player's stats.       ")
        print( "	     ================================================== ")
        print( "	          L   Lewandowski	M  Mbappe        ")
        print( "	          P   Perisic     	J  Jo        ")
        print( "	          R   Richarlison	X  Exit          ")
        print( "	     ================================================== ");
        choice = input( " Choose L, M, P, J, R or X please ==>              ")
        
        if choice  == 'L' or choice == 'l':
                allLewandowski = lewFacts.getLewandowski()
                lewFacts.calcAvgGoals(allLewandowski)
                lewFacts.getScore(allLewandowski)

        elif choice == 'M' or choice == 'm':
                allMbappe = mbaFacts.getMbappe()
                mbaFacts.calcAvgGoals(allMbappe)
                mbaFacts.getScore(allMbappe)
                
        elif choice == 'P' or choice == 'p':
                allPerisic = perFacts.getPerisic()
                perFacts.calcAvgGoals(allPerisic)
                perFacts.getScore(allPerisic)
                
        elif choice == 'J' or choice == 'j':
                allJo = joFacts.getJo()
                joFacts.calcAvgGoals(allJo)
                joFacts.getScore(allJo)
                
        elif choice == 'R' or choice == 'r':
                allRicharlison = ricFacts.getRicharlison()
                ricFacts.calcAvgGoals(allRicharlison)
                ricFacts.getScore(allRicharlison)

        elif choice == 'x' or choice == 'X':
                break
        else:
                print( "\n.. I did not understand you, try again!\n")
        #end if
                
#end while
print("\n...		    World Cup Qatar 2022!!!\n\n\n")

#end useClassSoccerFacts
