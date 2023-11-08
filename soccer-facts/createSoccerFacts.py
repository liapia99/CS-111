#   ======================================================================
#   File: createSoccerFacts.py
#   Purpose: Create a class file with functions of files
#   Name: Julia Piascik 
#   ======================================================================

class lewFacts:
    
    def getLewandowski():
        lewandowskiL = []
        lewandowskiFile = open("lewandowski.dat", 'r')
        for lewandowski in lewandowskiFile:
            lewandowski = lewandowski.split()
            lewandowskiL.append(lewandowski)
        #end for lewandowski
        lewandowskiFile.close()
        return lewandowskiL
    #end ftn getLewandowski

    def calcAvgGoals(allLewandowski):
        totalSum = 0
        goalsMade = 0
        goalsMissed = 0
        for lewandowski in allLewandowski:
            goalsMade = float(lewandowski[1])
            goalsMissed = float(lewandowski[2])
            goalsMade = goalsMade + 1
            goalsMissed = goalsMissed + 1
        sum = goalsMade + goalsMissed 
        #end for lewandowski
        m = (goalsMade/sum) * 100
        mis = (goalsMissed/sum) * 100
        print("Lewandowski made :", m,"% of his goals.")
        print("Lewandowski missed :", mis,"% of his goals.")
    #end ftn calcAvgGoal

    def getScore(allLewandowski):
        t = 0
        f = 0
        for lewandowski in allLewandowski:
            score = str(lewandowski[3])
            if score == 'False':
                f = 1 + f
            else:
                t = t + 1
            #endif
        #end for lewandowski
        print("Lewandowski won :", t," times.")
        print("Lewandowski lost :",f," times.")
    #end ftn getScore

#end class lewFacts

 

class mbaFacts:
    
    def getMbappe():
        mbappeL = []
        mbappeFile = open("mbappe.dat", 'r')
        for mbappe in mbappeFile:
            mbappe = mbappe.split()
            mbappeL.append(mbappe)
        #end for mbappe
        mbappeFile.close()
        return mbappeL
    #end ftn getMbappe

    def calcAvgGoals(allMbappe):
        totalSum = 0
        goalsMade = 0
        goalsMissed = 0
        for mbappe in allMbappe:
            goalsMade = float(mbappe[1])
            goalsMissed = float(mbappe[2])
            goalsMade = goalsMade + 1
            goalsMissed = goalsMissed + 1
        sum = goalsMade + goalsMissed 
        #end for mbappe
        m = (goalsMade/sum) * 100
        mis = (goalsMissed/sum) * 100
        print("Mbappe made :", m,"% of his goals.")
        print("Mbappe missed :", mis,"% of his goals.")
    #end ftn calcAvgGoal

    def getScore(allMbappe):
        t = 0
        f = 0
        for mbappe in allMbappe:
            score = str(mbappe[3])
            if score == 'False':
                f = 1 + f
            else:
                t = t + 1
            #endif
        #end for mbappe
        print("Mbappe won :", t," times.")
        print("Mbappe lost :",f," times.")
    #end ftn getScore
        
#end class mbaFacts

class perFacts:
    
    def getPerisic():
        perisicL = []
        perisicFile = open("perisic.dat", 'r')
        for perisic in perisicFile:
            perisic = perisic.split()
            perisicL.append(perisic)
        #end for perisic
        perisicFile.close()
        return perisicL
    #end ftn getPerisic

    def calcAvgGoals(allPerisic):
        totalSum = 0
        goalsMade = 0
        goalsMissed = 0
        for perisic in allPerisic:
            goalsMade = float(perisic[1])
            goalsMissed = float(perisic[2])
            goalsMade = goalsMade + 1
            goalsMissed = goalsMissed + 1
        sum = goalsMade + goalsMissed 
        #end for perisic
        m = (goalsMade/sum) * 100
        mis = (goalsMissed/sum) * 100
        print("Perisic made :", m,"% of his goals.")
        print("Perisic missed :", mis,"% of his goals.")
    #end ftn calcAvgGoal

    def getScore(allPerisic):
        t = 0
        f = 0
        for perisic in allPerisic:
            score = str(perisic[3])
            if score == 'False':
                f = 1 + f
            else:
                t = t + 1
            #endif
        #end for perisic
        print("Perisic won :", t," times.")
        print("Perisic lost :",f," times.")
    #end ftn getScore
        
#end class perFacts

class joFacts:
    
    def getJo():
        joL = []
        joFile = open("jo.dat", 'r')
        for jo in joFile:
            jo = jo.split()
            joL.append(jo)
        #end for jo
        joFile.close()
        return joL
    #end ftn getJo

    def calcAvgGoals(allJo):
        totalSum = 0
        goalsMade = 0
        goalsMissed = 0
        for jo in allJo:
            goalsMade = float(jo[1])
            goalsMissed = float(jo[2])
            goalsMade = goalsMade + 1
            goalsMissed = goalsMissed + 1
        sum = goalsMade + goalsMissed 
        #end for jo
        m = (goalsMade/sum) * 100
        mis = (goalsMissed/sum) * 100
        print("Jo made :", m,"% of his goals.")
        print("Jo missed :", mis,"% of his goals.")
    #end ftn calcAvgGoal

    def getScore(allJo):
        t = 0
        f = 0
        for jo in allJo:
            score = str(jo[3])
            if score == 'False':
                f = 1 + f
            else:
                t = t + 1
            #endif
        #end for jo
        print("Jo won :", t," times.")
        print("Jo lost :",f," times.")
    #end ftn getScore
        
#end class joFacts

class ricFacts:
    
    def getRicharlison():
        richarlisonL = []
        richarlisonFile = open("richarlison.dat", 'r')
        for richarlison in richarlisonFile:
            richarlison = richarlison.split()
            richarlisonL.append(richarlison)
        #end for richarlison
        richarlisonFile.close()
        return richarlisonL
    #end ftn getRicharlison

    def calcAvgGoals(allRicharlison):
        totalSum = 0
        goalsMade = 0
        goalsMissed = 0
        for richarlison in allRicharlison:
            goalsMade = float(richarlison[1])
            goalsMissed = float(richarlison[2])
            goalsMade = goalsMade + 1
            goalsMissed = goalsMissed + 1
        sum = goalsMade + goalsMissed 
        #end for richarlison
        m = (goalsMade/sum) * 100
        mis = (goalsMissed/sum) * 100
        print("Richarlison made :", m,"% of his goals.")
        print("Richarlison missed :", mis,"% of his goals.")
    #end ftn calcAvgGoal

    def getScore(allRicharlison):
        t = 0
        f = 0
        for richarlison in allRicharlison:
            score = str(richarlison[3])
            if score == 'False':
                f = 1 + f
            else:
                t = t + 1
            #endif
        #end for jo
        print("Richarlison won :", t," times.")
        print("Richarlison lost :",f," times.")
    #end ftn getScore
        
#end class ricFacts
