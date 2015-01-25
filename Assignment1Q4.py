

#Author : Bipra De
#Date : 7-Sep-2014

#PROBLEM STATEMENT

# Use the probabilities from the last experiment as distribution p.
# Then calculate the distribution q over the following text:
#
# "The sun never set on the British Empire because the British Empire is in the East and the sun sets in the West.
# Queen Victoria was the longest queen. She sat on a thorn for 63 years.
# He reclining years and finally the end of her life were exemplatory of a great personality.
# Her death was the final event which ended her reign."
#
# Replace all the zeroes by 0.0001.
# What is the KL divergence between the two distributions?

from __future__ import division
from Assignment1Q3 import dictionaryP,noOfAlphabets
import re
import math

inputString = '''The sun never set on the British Empire because the British Empire is in the East and the sun sets in the West.
Queen Victoria was the longest queen. She sat on a thorn for 63 years.
He reclining years and finally the end of her life were exemplatory of a great personality.
Her death was the final event which ended her reign.'''
dictionaryQ= dict()
noOfAlphabetsInQ=0
for i in range(0,len(inputString)):
    if re.match(r'[a-zA-Z]',inputString[i]):
        if inputString[i].lower() in dictionaryQ:
            dictionaryQ[inputString[i].lower()]+=1
        else:
            dictionaryQ[inputString[i].lower()]=1
        noOfAlphabetsInQ+=1

print
print
print "Map of letters and their relative frequency in P"
print dictionaryP,
print
print "Map of letters and their relative frequency in Q"
print dictionaryQ
print
print "Let X be the random Variable mapping all the unique letters from Input P and Q to numbers"
print
print "Letter"+" "*10+"Random variable X's value"+" "*8+"P(x)"+" "*10+"Q(x)"+" "*10+"P(x) . log[P(x)/Q(x)]"
print "-"*99
print
probabilityOfOccurence=0
result=0
count=1
keysList= dictionaryP.keys()
keysList=keysList+dictionaryQ.keys()
keysSet=set(keysList)

for key in keysSet:

    if key in dictionaryP:
        probabilityOfKeyInP=round(dictionaryP[key]/noOfAlphabets,4)

    else:
        probabilityOfKeyInP=0.0001

    if key in dictionaryQ:
        probabilityOfKeyInQ=round(dictionaryQ[key]/noOfAlphabetsInQ,4)
    else:
        probabilityOfKeyInQ=0.0001
    intermediateResult=round(probabilityOfKeyInP * math.log(probabilityOfKeyInP/probabilityOfKeyInQ, 2),4)
    result += intermediateResult
    print key+" "*22+str(count)+" "*25+str(probabilityOfKeyInP)+" "*9+str(probabilityOfKeyInQ)+" "*10+str(intermediateResult)
    count+=1
print
print "The KL divergence between the Distributions P and Q i.e. D(P||Q) is : "+str(round(result,4))