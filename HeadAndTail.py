"""
Distribution of random coin toss
"""

# https://januverma.wordpress.com/2014/12/13/gibbs-sampling/
from __future__ import division
import random

TestSize=1000
 
def sampler():
    r = random.random()
    if (r < 0.5):
        X = 0
    else:
        X = 1
    return X

ListOfTossResult = []

for N in range(TestSize):
	tossResult = sampler()
	ListOfTossResult.append(tossResult)

count0 = len([x for x in ListOfTossResult if x==0])
count1 = len([x for x in ListOfTossResult if x==1])
ratio0 = count0/len(ListOfTossResult)
ratio1 = count1/len(ListOfTossResult)

#print ListOfTossResult
print ratio0, ratio1

