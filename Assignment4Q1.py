#Author : Bipra De
#Date : 19-Oct-2014

#PROBLEM STATEMENT

# Forward / Backward Algorithm
# Consider the example of the HMM for POS tagging the sentence ”a myth is a female moth”.
# Given the  intitial vector, transition matrix and emission matrix,
# Calculate the following forward accumulators given the following probabilities.
#
# (a) α4(NN)
# (b) α3(VB)
# (c) α1(DT)
# (d) β4(NN)
# (e) β3(NN)

from collections import namedtuple

v = [0.45, 0.35, 0.15, 0.05]            #Initial Vector storing initial probabilities for DT, JJ, NN, VB

#Creating lexical probability dictionary
wordPOSCombo=namedtuple('wordPOSCombo', ['word', 'POS'])
lexicalProbabilityDictionary=dict()

lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='DT')] = 0.85
lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='JJ')] = 0.05
lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='NN')] = 0.03
lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='VB')] = 0.05

lexicalProbabilityDictionary[wordPOSCombo(word='myth', POS='DT')] = 0.01
lexicalProbabilityDictionary[wordPOSCombo(word='myth', POS='JJ')] = 0.10
lexicalProbabilityDictionary[wordPOSCombo(word='myth', POS='NN')] = 0.45
lexicalProbabilityDictionary[wordPOSCombo(word='myth', POS='VB')] = 0.10

lexicalProbabilityDictionary[wordPOSCombo(word='is', POS='DT')] = 0.02
lexicalProbabilityDictionary[wordPOSCombo(word='is', POS='JJ')] = 0.02
lexicalProbabilityDictionary[wordPOSCombo(word='is', POS='NN')] = 0.02
lexicalProbabilityDictionary[wordPOSCombo(word='is', POS='VB')] = 0.60

lexicalProbabilityDictionary[wordPOSCombo(word='female', POS='DT')] = 0.01
lexicalProbabilityDictionary[wordPOSCombo(word='female', POS='JJ')] = 0.60
lexicalProbabilityDictionary[wordPOSCombo(word='female', POS='NN')] = 0.25
lexicalProbabilityDictionary[wordPOSCombo(word='female', POS='VB')] = 0.05

lexicalProbabilityDictionary[wordPOSCombo(word='moth', POS='DT')] = 0.12
lexicalProbabilityDictionary[wordPOSCombo(word='moth', POS='JJ')] = 0.13
lexicalProbabilityDictionary[wordPOSCombo(word='moth', POS='NN')] = 0.25
lexicalProbabilityDictionary[wordPOSCombo(word='moth', POS='VB')] = 0.20

#Creating transition probability dictionary
state1State2=namedtuple('state1State2', ['state1', 'state2'])
transitionProbabilityDictionary=dict()

transitionProbabilityDictionary[state1State2(state1='DT', state2='DT')] = 0.03
transitionProbabilityDictionary[state1State2(state1='DT', state2='JJ')] = 0.42
transitionProbabilityDictionary[state1State2(state1='DT', state2='NN')] = 0.50
transitionProbabilityDictionary[state1State2(state1='DT', state2='VB')] = 0.05

transitionProbabilityDictionary[state1State2(state1='JJ', state2='DT')] = 0.01
transitionProbabilityDictionary[state1State2(state1='JJ', state2='JJ')] = 0.25
transitionProbabilityDictionary[state1State2(state1='JJ', state2='NN')] = 0.65
transitionProbabilityDictionary[state1State2(state1='JJ', state2='VB')] = 0.09

transitionProbabilityDictionary[state1State2(state1='NN', state2='DT')] = 0.07
transitionProbabilityDictionary[state1State2(state1='NN', state2='JJ')] = 0.03
transitionProbabilityDictionary[state1State2(state1='NN', state2='NN')] = 0.15
transitionProbabilityDictionary[state1State2(state1='NN', state2='VB')] = 0.75

transitionProbabilityDictionary[state1State2(state1='VB', state2='DT')] = 0.30
transitionProbabilityDictionary[state1State2(state1='VB', state2='JJ')] = 0.25
transitionProbabilityDictionary[state1State2(state1='VB', state2='NN')] = 0.15
transitionProbabilityDictionary[state1State2(state1='VB', state2='VB')] = 0.30

inputString='a myth is a female moth'
inputString=inputString.split(' ')

alpha = dict()        #Stores an array for all forward variable values. alpha[i][j] denotes the value of the forward variable at time i and state j
a = dict()
a['DT']=v[0] * lexicalProbabilityDictionary[wordPOSCombo(word=inputString[0], POS='DT')]
a['JJ']=v[1] * lexicalProbabilityDictionary[wordPOSCombo(word=inputString[0], POS='JJ')]
a['NN']=v[2] * lexicalProbabilityDictionary[wordPOSCombo(word=inputString[0], POS='NN')]
a['VB']=v[3] * lexicalProbabilityDictionary[wordPOSCombo(word=inputString[0], POS='VB')]

alpha[1]=a                          #alpha1 for all possible 4 states
for i in range(2,7):
    b=dict()

    b['DT'] = (alpha[i-1]['DT'] * transitionProbabilityDictionary[state1State2(state1='DT', state2='DT')]+alpha[i-1]['JJ']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='DT')]+alpha[i-1]['NN']*transitionProbabilityDictionary[state1State2(state1='NN', state2='DT')]+alpha[i-1]['VB']*transitionProbabilityDictionary[state1State2(state1='VB', state2='DT')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='DT')]
    b['JJ'] = (alpha[i-1]['DT'] * transitionProbabilityDictionary[state1State2(state1='DT', state2='JJ')]+alpha[i-1]['JJ']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='JJ')]+alpha[i-1]['NN']*transitionProbabilityDictionary[state1State2(state1='NN', state2='JJ')]+alpha[i-1]['VB']*transitionProbabilityDictionary[state1State2(state1='VB', state2='JJ')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='JJ')]
    b['NN'] = (alpha[i-1]['DT'] * transitionProbabilityDictionary[state1State2(state1='DT', state2='NN')]+alpha[i-1]['JJ']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='NN')]+alpha[i-1]['NN']*transitionProbabilityDictionary[state1State2(state1='NN', state2='NN')]+alpha[i-1]['VB']*transitionProbabilityDictionary[state1State2(state1='VB', state2='NN')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='NN')]
    b['VB'] = (alpha[i-1]['DT'] * transitionProbabilityDictionary[state1State2(state1='DT', state2='VB')]+alpha[i-1]['JJ']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='VB')]+alpha[i-1]['NN']*transitionProbabilityDictionary[state1State2(state1='NN', state2='VB')]+alpha[i-1]['VB']*transitionProbabilityDictionary[state1State2(state1='VB', state2='VB')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='VB')]
    alpha[i] = b


print
print "(a) For Computing "+unichr(0x3b1).encode('utf-8')+"4"+"(NN) : "
print "We used the equation "
print
print "["+unichr(0x3b1).encode('utf-8')+"3"+"(DT) * P(NN|DT) + "+unichr(0x3b1).encode('utf-8')+"3"+"(JJ) * P(NN|JJ) + "+unichr(0x3b1).encode('utf-8')+"3"+"(NN) * P(NN|NN) + "+unichr(0x3b1).encode('utf-8')+"3"+"(VB) * P(NN|VB)]* P(a|NN)"
print
print "Substituting the values in the above equation : "
print
print "["+str(alpha[3]['DT'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='DT', state2='NN')])+" + "+str(alpha[3]['JJ'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='JJ', state2='NN')])+" + "+str(alpha[3]['NN'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='NN')])+" + "+str(alpha[3]['VB'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='VB', state2='NN')])+"]"+" * "+str(lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='NN')])
print
print "= "+str(alpha[4]['NN'])
print
print "#"*100
print
print "(b) For Computing "+unichr(0x3b1).encode('utf-8')+"3"+"(VB) : "
print "We used the equation "
print
print "["+unichr(0x3b1).encode('utf-8')+"2"+"(DT) * P(VB|DT) + "+unichr(0x3b1).encode('utf-8')+"2"+"(JJ) * P(VB|JJ) + "+unichr(0x3b1).encode('utf-8')+"2"+"(NN) * P(VB|NN) + "+unichr(0x3b1).encode('utf-8')+"2"+"(VB) * P(VB|VB)]* P(is|NN)"
print
print "Substituting the values in the above equation : "
print
print "["+str(alpha[2]['DT'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='DT', state2='VB')])+" + "+str(alpha[2]['JJ'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='JJ', state2='VB')])+" + "+str(alpha[2]['NN'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='VB')])+" + "+str(alpha[2]['VB'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='VB', state2='VB')])+"]"+" * "+str(lexicalProbabilityDictionary[wordPOSCombo(word='is', POS='VB')])
print
print "= "+str(alpha[3]['VB'])
print
print "#"*100
print
print "(c) For Computing "+unichr(0x3b1).encode('utf-8')+"1"+"(DT) : "
print "We used the equation "
print
print "P(DT|State 1) * P(a|DT)"
print
print "Substituting the values in the above equation : "
print
print str(v[0])+" * "+str(lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='DT')])
print
print "= "+str(alpha[1]['DT'])

beta=dict()              #Stores an array for all backward variable values. beta[i][j] denotes the value of the backward variable at time i and state j
beta[6]={'DT':1,'JJ':1,'NN':1,'VB':1}           #stores beta(6) values for all the possible states at time 6
for i in range(5,0,-1):
    c=dict()
    c['DT']=(beta[i+1]['DT']*transitionProbabilityDictionary[state1State2(state1='DT', state2='DT')]+beta[i+1]['JJ']*transitionProbabilityDictionary[state1State2(state1='DT', state2='JJ')]+beta[i+1]['NN']*transitionProbabilityDictionary[state1State2(state1='DT', state2='NN')]+beta[i+1]['VB']*transitionProbabilityDictionary[state1State2(state1='DT', state2='VB')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='DT')]
    c['JJ']=(beta[i+1]['DT']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='DT')]+beta[i+1]['JJ']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='JJ')]+beta[i+1]['NN']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='NN')]+beta[i+1]['VB']*transitionProbabilityDictionary[state1State2(state1='JJ', state2='VB')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='JJ')]
    c['NN']=(beta[i+1]['DT']*transitionProbabilityDictionary[state1State2(state1='NN', state2='DT')]+beta[i+1]['JJ']*transitionProbabilityDictionary[state1State2(state1='NN', state2='JJ')]+beta[i+1]['NN']*transitionProbabilityDictionary[state1State2(state1='NN', state2='NN')]+beta[i+1]['VB']*transitionProbabilityDictionary[state1State2(state1='NN', state2='VB')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='NN')]
    c['VB']=(beta[i+1]['DT']*transitionProbabilityDictionary[state1State2(state1='VB', state2='DT')]+beta[i+1]['JJ']*transitionProbabilityDictionary[state1State2(state1='VB', state2='JJ')]+beta[i+1]['NN']*transitionProbabilityDictionary[state1State2(state1='VB', state2='NN')]+beta[i+1]['VB']*transitionProbabilityDictionary[state1State2(state1='VB', state2='VB')])*lexicalProbabilityDictionary[wordPOSCombo(word=inputString[i-1], POS='VB')]
    beta[i]=c
print
print "#"*100
print
print "(d) For Computing "+unichr(0x3b2).encode('utf-8')+"4"+"(NN) : "
print "We used the equation "
print
print "["+unichr(0x3b2).encode('utf-8')+"5"+"(DT) * P(DT|NN) + "+unichr(0x3b2).encode('utf-8')+"5"+"(JJ) * P(JJ|NN) + "+unichr(0x3b2).encode('utf-8')+"5"+"(NN) * P(NN|NN) + "+unichr(0x3b2).encode('utf-8')+"5"+"(VB) * P(VB|NN)]* P(is|NN)"
print
print "Substituting the values in the above equation : "
print
print "["+str(beta[5]['DT'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='DT')])+" + "+str(beta[5]['JJ'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='JJ')])+" + "+str(beta[5]['NN'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='NN')])+" + "+str(beta[5]['VB'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='VB')])+"]"+" * "+str(lexicalProbabilityDictionary[wordPOSCombo(word='is', POS='NN')])
print
print "= "+str(beta[4]['NN'])
print
print "#"*100
print
print "(e) For Computing "+unichr(0x3b2).encode('utf-8')+"3"+"(NN) : "
print "We used the equation "
print
print "["+unichr(0x3b2).encode('utf-8')+"4"+"(DT) * P(DT|NN) + "+unichr(0x3b2).encode('utf-8')+"4"+"(JJ) * P(JJ|NN) + "+unichr(0x3b2).encode('utf-8')+"4"+"(NN) * P(NN|NN) + "+unichr(0x3b2).encode('utf-8')+"4"+"(VB) * P(VB|NN)]* P(a|NN)"
print
print "Substituting the values in the above equation : "
print
print "["+str(beta[4]['DT'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='DT')])+" + "+str(beta[4]['JJ'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='JJ')])+" + "+str(beta[4]['NN'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='NN')])+" + "+str(beta[4]['VB'])+" * "+str(transitionProbabilityDictionary[state1State2(state1='NN', state2='VB')])+"]"+" * "+str(lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='NN')])
print
print "= "+str(beta[3]['NN'])
