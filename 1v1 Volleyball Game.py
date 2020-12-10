from random import random
import statistics
#Start represents which player starts on the recieving side
#A and B represend the hitting percentages for players A and B
#x represents how many rounds per practice
#y represents the number of practices
def main(start, A, B, x, y):
    #Scores start at 0 and add 1 each time a player gets a kill
    #Initializing variables
    SrA = A
    SrB = B
    FrA = A
    FrB = B
    scoreA = 0
    scoreB = 0
    AScoreTotal = 0
    BScoreTotal = 0
    AWins = 0
    BWins = 0
    ScoreDiffA = 0
    DiffListA = []
    ScoreDiffB = 0
    DiffListB = []
    AWinsList = []
    BWinsList = []
    avgAwins = 0
    avgBwins = 0
    SDAwins = 0
    SDBwins = 0
    APractices = 0
    BPractices = 0
    ties = 0
    #if lastpoint = 0, this means A scored last
    #if lastpoint = 1, this means B scored last
    lastpoint = 0
    #run_num determines whether a free ball is given
    run_num = 1
    for j in range(0,y):
        for i in range(0,x):
            #Serve recieve ball
            while scoreA == 0 and scoreB == 0:
                #Case where player A is recieving
                if start == "A":
                    if random() < SrA:
                        scoreA += 1
                        lastpoint = 0
                        #Winning SR makes run_num 0 to get a free ball
                        run_num = 0
                    else:
                        #Washing SR makes lastpoint 1 so player B gets next turn
                        lastpoint = 1
                        #Washing SR makes run_num 1 go go to rally play
                        run_num = 1
                        break
                #Case where player B is recieving
                if start == "B":
                    if random() < SrB:
                        scoreB += 1
                        lastpoint = 1
                        run_num = 0
                    else:
                        lastpoint = 0
                        run_num = 1
                        break
            #Everything that isnt the serve ball
            while scoreA  < 3 and scoreB < 3:
                #Player A gets to start since they scored the last point
                if lastpoint == 0:
                    while True:
                        #Free ball happens when run_num is 0
                        if run_num == 0:
                            if random() < FrA:
                                scoreA += 1
                                #run num is 0 to get another free ball after the kill
                                run_num = 0
                                break
                            else:
                                #lastpoint is changed so B goes next if A washes free
                                lastpoint = 1
                                #run_num is 1 if washed so we go to rally play
                                run_num = 1
                                break
                        #rally play where A starts
                        if random() < A:
                            scoreA += 1
                            lastpoint = 0
                            run_num = 0
                            break
                        if random() < B:
                            scoreB += 1
                            lastpoint = 1
                            run_num = 0
                            break
                #Player B gets to start since they scored the last point
                elif lastpoint == 1:
                    while True:
                        #Free ball
                        if run_num == 0:
                            if random() < FrB:
                                scoreB += 1
                                run_num = 0
                                break
                            else:
                                lastpoint = 0
                                run_num = 1
                                break
                        #rally play where B starts
                        if random() < B:
                            scoreB += 1
                            lastpoint = 1
                            run_num = 0
                            break
                        if random() < A:
                            scoreA += 1
                            lastpoint = 0
                            run_num = 0
                            break 
            AScoreTotal += scoreA
            BScoreTotal += scoreB
            if scoreA > scoreB:
                AWins += 1
                ScoreDiffA = scoreA-scoreB
                DiffListA.append(ScoreDiffA)
            if scoreB > scoreA:
                BWins += 1
                ScoreDiffB = scoreB-scoreA
                DiffListB.append(ScoreDiffB)
            scoreA = 0
            scoreB = 0
        q = 0
        u = 0
        for i in DiffListA:
            q += i
        for i in DiffListB:
            u += i
        if len(DiffListA) == 0:
            AvgDiffA = "NA"
        else:
            AvgDiffA = q/len(DiffListA)
        if len(DiffListB) == 0:
            AvgDiffB = "NA"
        else:
            AvgDiffB = u/len(DiffListB)
        #This shows the summary from each practice
        """print("Avg A Diff:", AvgDiffA, "Avg B Diff:", AvgDiffB)
        print("A Total:", AScoreTotal ,"B Total:", BScoreTotal)
        print("A Wins:",AWins,"B Wins:",BWins)
        print("")"""
        AWinsList.append(AWins)
        BWinsList.append(BWins)
        if AWins > BWins:
            APractices += 1
        elif BWins > AWins:
            BPractices += 1
        else:
            ties += 1
            
        AWins = 0
        BWins = 0
        AScoreTotal = 0
        BScoreTotal = 0
        AvgDiffA = 0
        AvgDiffB = 0
    avgAwins = statistics.mean(AWinsList)
    SDAwins = statistics.stdev(AWinsList)
    avgBwins = statistics.mean(BWinsList)
    SDBwins = statistics.stdev(BWinsList)
    #This shows the summary across many practices
    print("End Summary:")
    print("Avg A wins per practice:", avgAwins, "Std Dev: ", SDAwins)
    print("Avg B wins per practice:", avgBwins, "Std Dev: ", SDBwins)
    print("A Practices: ",APractices, "B Practices: ",BPractices, "Ties: ",ties)
    
        
