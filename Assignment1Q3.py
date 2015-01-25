
#Author : Bipra De
#Date : 7-Sep-2014

#PROBLEM STATEMENT

# Take the following text and
#
# (a) calculate the probabilities of the letters (approximated by their relative frequencies). Ignore punctu- ation signs and numbers.
#     Treat upper case and lower case letters as equal.
# (b) come up with a random variable for the letters and write it down. How many digits do you need?
# (c) calculate the Expected Value and the Variance of this code.
#
# "Bach was the most famous composer in the world, and so was Handel.
# Handel was half German, half Italian and half English. He was very large.
# Bach died from 1750 to the present. Beethoven wrote music even though he was deaf.
# He was so deaf he wrote loud music. He took long walks in the forest even when everyone was calling for him.
# Beethoven expired in 1827 and later died for this."



from __future__ import division
import re

inputString = '''Bach was the most famous composer in the world, and so was Handel.
Handel was half German, half Italian and half English. He was very large.
Bach died from 1750 to the present. Beethoven wrote music even though he was deaf.
He was so deaf he wrote loud music. He took long walks in the forest even when everyone was calling for him.
Beethoven expired in 1827 and later died for this.'''
dictionaryP= dict()
noOfAlphabets=0;
for i in range(0,len(inputString)):
    if re.match(r'[a-zA-Z]',inputString[i]):
        if inputString[i].lower() in dictionaryP:
            dictionaryP[inputString[i].lower()]+=1
        else:
            dictionaryP[inputString[i].lower()]=1
        noOfAlphabets+=1

print "Map of letters and their frequency"
print
print dictionaryP
print
print "Total number of alphabets in the input sentence :  "+str(noOfAlphabets)
print
print "Let X be the random variable"
print
print "Letter"+" "*10+"Random variable X's value"+" "*10+"Probability of Occurence"+" "*10+"x.p(x)"+" "*10+"x^2 . p(x)"
print "-"*112
randomVariable=1
probabilityOfOccurence=0
expectation=0
expectationForXSquare=0
for key in dictionaryP:
    probabilityOfOccurence=dictionaryP[key]/noOfAlphabets
    print key+" "*20+str(randomVariable)+" "*40+"%.3f" % round(probabilityOfOccurence,3)+" "*20+"%.3f" % (randomVariable*probabilityOfOccurence)+" "*10+"%.3f" % ((randomVariable**2)*probabilityOfOccurence)
    randomVariable+=1
    expectation+=randomVariable*probabilityOfOccurence
    expectationForXSquare+=(randomVariable**2)*probabilityOfOccurence

print
print "Total digits required for Random Variable(X) : "+str(2)

print
print "Expectation of the Random variable X i.e. E(X) : "+"%.3f"%expectation

print
print"Variance of the Random variable X : E(X^2)-[E(X)]^2 = "+"%.3f"%float(expectationForXSquare-expectation**2)







