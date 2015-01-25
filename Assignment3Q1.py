#Author : Bipra De
#Date : 9-Oct-2014

#PROBLEM STATEMENT

# Bigram Tagging
# Given the probabilities in the table below, what is the probability of the following tag sequences for the sentence time flies like an arrow?
# Note that the probabilities are shown as percentage (0-100%).
# (a) VB NNS IN DT NN
# (b) JJ VBZ VB DT NN




from __future__ import division
from collections import namedtuple

#Creating a dictionary of the given probabilities



#Creating lexical probability dictionary
wordPOSCombo=namedtuple('wordPOSCombo', ['word', 'POS'])
lexicalProbabilityDictionary=dict()

lexicalProbabilityDictionary[wordPOSCombo(word='time', POS='NN')] = 7.0727/100
lexicalProbabilityDictionary[wordPOSCombo(word='time', POS='VB')] = 0.0005/100
lexicalProbabilityDictionary[wordPOSCombo(word='time', POS='JJ')] = 0/100
lexicalProbabilityDictionary[wordPOSCombo(word='flies', POS='VBZ')] = 0.4754/100
lexicalProbabilityDictionary[wordPOSCombo(word='flies', POS='NNS')] = 0.1610/100
lexicalProbabilityDictionary[wordPOSCombo(word='like', POS='IN')] = 2.6512/100
lexicalProbabilityDictionary[wordPOSCombo(word='like', POS='VB')] = 2.8413/100
lexicalProbabilityDictionary[wordPOSCombo(word='like', POS='RB')] = 0.5086/100
lexicalProbabilityDictionary[wordPOSCombo(word='an', POS='DT')] = 1.4192/100
lexicalProbabilityDictionary[wordPOSCombo(word='arrow', POS='NN')] = 0.0215/100
lexicalProbabilityDictionary[wordPOSCombo(word='arrow', POS='NN')] = 0.0215/100


#Creating transition probability dictionary
state1State2=namedtuple('state1State2', ['state2', 'state1'])
transitionProbabilityDictionary=dict()

transitionProbabilityDictionary[state1State2(state2='NN', state1='S')] = 0.6823/100
transitionProbabilityDictionary[state1State2(state2='VB', state1='S')] = 0.5294/100
transitionProbabilityDictionary[state1State2(state2='JJ', state1='S')] = 0.8033/100
transitionProbabilityDictionary[state1State2(state2='VBZ', state1='NN')] = 3.9005/100
transitionProbabilityDictionary[state1State2(state2='VBZ', state1='VB')] = 0.0566/100
transitionProbabilityDictionary[state1State2(state2='VBZ', state1='JJ')] = 2.0934/100
transitionProbabilityDictionary[state1State2(state2='NNS', state1='NN')] = 1.6076/100
transitionProbabilityDictionary[state1State2(state2='NNS', state1='VB')] = 0.6566/100
transitionProbabilityDictionary[state1State2(state2='NNS', state1='JJ')] = 2.4383/100
transitionProbabilityDictionary[state1State2(state2='IN', state1='VBZ')] = 8.5862/100
transitionProbabilityDictionary[state1State2(state2='IN', state1='NNS')] = 21.8302/100
transitionProbabilityDictionary[state1State2(state2='VB', state1='VBZ')] = 0.7002/100
transitionProbabilityDictionary[state1State2(state2='VB', state1='NNS')] = 11.1406/100
transitionProbabilityDictionary[state1State2(state2='VB', state1='NNS')] = 11.1406/100
transitionProbabilityDictionary[state1State2(state2='RB', state1='VBZ')] = 15.0350/100
transitionProbabilityDictionary[state1State2(state2='RB', state1='NNS')] = 6.4721/100
transitionProbabilityDictionary[state1State2(state2='DT', state1='IN')] = 31.4263/100
transitionProbabilityDictionary[state1State2(state2='DT', state1='VB')] = 15.2649/100
transitionProbabilityDictionary[state1State2(state2='DT', state1='RB')] = 5.3113/100
transitionProbabilityDictionary[state1State2(state2='NN', state1='DT')] = 38.0170/100
transitionProbabilityDictionary[state1State2(state2='E', state1='NN')] = 0.2069/100

#Tag Sequences whose probability of occurrence needs to be computed
tagSequence1 = ['S', 'VB', 'NNS', 'IN', 'DT', 'NN', 'E']
tagSequence2 = ['S', 'JJ', 'VBZ', 'VB', 'DT', 'NN', 'E']

#Input sentence
sentence = 'time flies like an arrow'
words = sentence.split(" ")

#Computing probability for tag sequence 1

probabilityOfTagSequence = 1
i = 0
for term in words:
    probabilityOfTagSequence = probabilityOfTagSequence * transitionProbabilityDictionary[state1State2(state2=tagSequence1[i+1], state1=tagSequence1[i])] * lexicalProbabilityDictionary[wordPOSCombo(word=term, POS=tagSequence1[i+1])]
    i += 1
probabilityOfTagSequence = probabilityOfTagSequence * transitionProbabilityDictionary[state1State2(state2=tagSequence1[i+1], state1=tagSequence1[i])]
print
print "INPUT STRING : "+sentence
print
print "#" * 30+" OUTPUT "+"#" * 34
print
print "Probability of tag sequence "+str(tagSequence1)
print probabilityOfTagSequence
print
print "Approximately equal to "
print '{0:.30f}'.format(probabilityOfTagSequence)
print
print "#" * 72

#Computing probability of tag sequence 2

probabilityOfTagSequence = 1
i = 0
for term in words:
    probabilityOfTagSequence = probabilityOfTagSequence * transitionProbabilityDictionary[state1State2(state2=tagSequence2[i+1], state1=tagSequence2[i])] * lexicalProbabilityDictionary[wordPOSCombo(word=term, POS=tagSequence2[i+1])]
    i += 1
probabilityOfTagSequence = probabilityOfTagSequence * transitionProbabilityDictionary[state1State2(state2=tagSequence2[i+1], state1=tagSequence2[i])]
print
print "Probability of tag sequence "+str(tagSequence2)
print probabilityOfTagSequence
print
print "#" * 72








