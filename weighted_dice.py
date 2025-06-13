from collections import defaultdict
from scipy import stats

observedRolls = [1,2,3,4,5,6]

numSides = 6
numRolls = len(observedRolls)
# Degrees of freedom for a goodness-of-fit test should be based on the
# number of categories, not the sample size.
degreesOfFreedom = numSides - 1
pValue = 0.05 

def expectedRollCounts(numRolls, numSides):
    out = {}
    for side in range(1, numSides+1):
        out[side] = numRolls / numSides
    return out

def observedRollCounts(observedRolls):
    out = defaultdict(lambda: 0)
    for roll in observedRolls:
        out[roll] += 1
    return out

def xc2(observedRollCounts, expectedRollCounts):
    out = 0
    for side in expectedRollCounts:
        o = observedRollCounts[side]
        e = expectedRollCounts[side]
        out += ((o - e) ** 2) / e
    return out

val = xc2(observedRollCounts(observedRolls), expectedRollCounts(numRolls, numSides))
print(val)
