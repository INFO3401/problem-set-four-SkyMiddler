from problemSet4 import *
from pollingData import *


#3) 1. Sanders and Biden have the most amount of votes
#   2. Sanders and Biden are the only two with spread
#   3. Styer and Gabbard have the least amount of votes

#4)
cleanedData = loadAndCleanData("politicsDemNom.csv")
#print(cleanedData.head())
#6)
normalData = normalizeData(cleanedData)
#print(normalData)

#7.cont)
"""
plotCandidate("Sanders", normalData)
plotCandidate("Biden", normalData)
plotCandidate("Bloomberg", normalData)
plotCandidate("Warren", normalData)
plotCandidate("Buttigieg", normalData)
plotCandidate("Klobuchar", normalData)
plotCandidate("Steyer", normalData)
plotCandidate("Gabbard", normalData
"""
#Biden and Sanders have the best polling numbers

#9)
candidateList = []

for candidate in normalData.columns:
    if candidate not in ['Poll', 'Date', 'Sample', 'Spread', 'Undecided']:
        candidateList.append(candidate)
        print(candidate, statsPerCandidate(candidate, normalData))

#Biden has the highest polling average

#11)
cleanSampleData = cleanSample(normalData)

#12) TEST
computePollWeight(cleanSampleData, "CNNCNN")

#14)
for candidate in candidateList:
    print(candidate, "->", weightedStatsPerCandidate(candidate, normalData))


#16)
repeats = []
for candidate1 in candidateList:
    for candidate2 in candidateList:
        if candidate1 != candidate2:
            if [candidate1,candidate2] not in repeats and [candidate2, candidate1] not in repeats:
                print(candidate1, "and", candidate2, "have a corrleation of", computeCorrelation(candidate1, candidate2, normalData))
                repeats.append([candidate1, candidate2])

#Biden and Klobuchar have the most correlation
#Sanders and Styer have the least correlation

#18)
superTuesday(normalData, candidateList)
print("Biden's mean is", int(normalData["BidenST"].mean()))
print("Sanders' mean is", int(normalData["SandersST"].mean()))
print("Biden's weighted mean is", int(weightedStatsPerCandidate("BidenST", normalData)))
print("Sanders' weighted mean is", int(weightedStatsPerCandidate("SandersST", normalData)))
#Looking at both it appears that Biden is winning

#19
print("The confidence interval for Biden is", getConfidenceIntervals(normalData["BidenST"]))
print("The confidence interval for Sanders is", getConfidenceIntervals(normalData["SandersST"]))
#Sanders has a higher confidence interval

#20
print(runTTest(normalData["Biden"], normalData["Sanders"]))
print(runTTest(normalData["BidenST"], normalData["SandersST"]))

#22
"""
Biden's mean is higher while Sanders is lower
Both have lower weighted means but Biden is still ahead of Sanders
Both have higher confidence intervals but Biden is now ahead of Sanders

This seemed to be an okay prediction, Biden passed Sanders confidence interval
after super Tuesday but the mean and weighted means show that Biden is now farther ahead
than Sanders. This shows that the correlation for problem 17 ended up being fairly accurate.
"""
