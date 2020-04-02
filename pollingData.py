import pandas as pd
import pprint as pprint
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
#5)
def normalizeData(dataFrame):
    undecided = []
    for i, x in dataFrame.iterrows():
        undecided.append((100-(x[3] + x[4])))
    dataFrame["Undecided"] = undecided
    return dataFrame

#7
def plotCandidate(candidate, dataFrame):
    plots = plt.scatter(x = dataFrame["Poll"], y = dataFrame[candidate])
    plt.show(plots)

#8
def statsPerCandidate(candidate ,dataFrame):
    avgPoll = dataFrame[candidate].mean()
    print(avgPoll)
    return avgPoll

#10)
def cleanSample(dataFrame):
    sampleType = []
    sampleSize = []
    for i in dataFrame["Sample"]:
        sampleType.append(i[-2:])
        sampleSize.append(i[:-2])
    for i in range(len(sampleSize)):
        if sampleSize[i] == '':
            sampleSize[i] = 0
        else:
            sampleSize[i] = int(sampleSize[i])
    dataFrame["Sample Type"] = sampleType
    dataFrame["Sample Size"] = sampleSize
    replacedData = dataFrame.replace({'':None})
    return replacedData

#12)
def computePollWeight(dataFrame, pollName):
    return sum(dataFrame[dataFrame['Poll'] == pollName]["Sample Size"]) / sum(dataFrame["Sample Size"])

#13)
def weightedStatsPerCandidate(candidate, dataFrame):
    weighted = []
    for poll in dataFrame["Poll"].unique():
        x = sum(dataFrame[dataFrame["Poll"] == poll][candidate])
        y = computePollWeight(dataFrame, poll)
        weighted.append(x*y)
    return sum(weighted)/len(weighted)

#15)
def computeCorrelation(candidate1, candidate2, dataFrame):
    return dataFrame[candidate1].corr(dataFrame[candidate2])

#17)

def superTuesday(dataFrame, candidateList):
    bidenST = []
    sandersST = []

    for i, x in dataFrame.iterrows():
        bCount = x["Biden"]
        sCount = x["Sanders"]

        for candidate in candidateList:
            if candidate != "Biden" and candidate != "Sanders":
                bCorr = computeCorrelation("Biden", candidate, dataFrame)
                sCorr = computeCorrelation("Sanders", candidate, dataFrame)

                if abs(bCorr) > abs(sCorr):
                    bCount += x[candidate]
                else:
                    sCount += x[candidate]
        bidenST.append(bCount)
        sandersST.append(sCount)
    dataFrame["BidenST"] = bidenST
    dataFrame["SandersST"] = sandersST

#19)
def getConfidenceIntervals(column):
    npArray = 1.0 * np.array(column)
    stdErr = scipy.stats.sem(npArray)
    n = len(column)
    return stdErr * scipy.stats.t.ppf((1+.95)/2.0,n-1)

#20)
def runTTest(data1, data2):
    return scipy.stats.ttest_ind(data1, data2)
