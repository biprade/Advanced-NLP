#Author : Bipra De
#Date : 19-Dec-2014

#PROBLEM STATEMENT

# Write a program that reestimates the first n rounds of Baum-Welch for the signal sequence ”a female moth is a myth”.
# The intial vector, transition matrix and emmission matrix are provided.

from __future__ import division
from collections import namedtuple

#Baum-Welch algorithm
inputSentence=input("Enter the input sentence ")

print
setOfWords=inputSentence.split(" ")
c=1
#States are DT,JJ,NN,VB
states=['DT','JJ','NN','VB']
#first HMM
initialProbability=dict()
initialProbability['DT']=0.45
initialProbability['JJ']=0.35
initialProbability['NN']=0.15
initialProbability['VB']=0.05

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

#Take number of rounds as input from the user
numberOfIerations=input("Enter number of rounds\n")

for z in range(0,numberOfIerations):

        #Computing alphas
        alpha=dict()

        alpha[(inputSentence,1,'DT')]=lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='DT')] * initialProbability['DT']
        alpha[(inputSentence,1,'JJ')]=lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='JJ')] * initialProbability['JJ']
        alpha[(inputSentence,1,'NN')]=lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='NN')] * initialProbability['NN']
        alpha[(inputSentence,1,'VB')]=lexicalProbabilityDictionary[wordPOSCombo(word='a', POS='VB')] * initialProbability['VB']

        for m in range(2,len(setOfWords)+1): #to loop over each words in the input sentence i.e. j
            for i in range(0,len(states)):  #to loop over each state for a  : LHS

                k=(inputSentence,m,states[i])
                alpha[k]=0
                for j in range(0,len(states)):#to loop over each component for calculating alpha
                    alpha[k]+=alpha[(inputSentence,m-1,states[j])] * transitionProbabilityDictionary[state1State2(state1=states[j], state2=states[i])] * lexicalProbabilityDictionary[wordPOSCombo(word=setOfWords[m-1], POS=states[i])]

        probabilityOfObservedSequence=0
        for i in range(0,len(states)):
            probabilityOfObservedSequence+=alpha[(inputSentence,len(setOfWords),states[i])]

        #Computing betas
        beta=dict()
        beta[(inputSentence,6,'DT')]=1
        beta[(inputSentence,6,'JJ')]=1
        beta[(inputSentence,6,'NN')]=1
        beta[(inputSentence,6,'VB')]=1

        for m in range(len(setOfWords)-1,0,-1):
            for i in range(0,len(states)):
                k=(inputSentence,m,states[i])
                beta[k]=0
                for j in range(0,len(states)):

                    beta[k] = beta[k] + beta[(inputSentence,m+1,states[j])] * transitionProbabilityDictionary[state1State2(state1=states[i], state2=states[j])] * lexicalProbabilityDictionary[wordPOSCombo(word=setOfWords[m], POS=states[j])]


        #calculating gammas
        gamma=dict()
        for m in range(1,len(setOfWords)): #to loop over all words
            for j in range(0,len(states)):
                for k in range(0,len(states)):
                    gamma[(inputSentence,m,states[j],states[k])]=alpha[(inputSentence,m,states[j])] * transitionProbabilityDictionary[state1State2(state1=states[j], state2=states[k])] * lexicalProbabilityDictionary[wordPOSCombo(word=setOfWords[m], POS=states[k])] * beta[(inputSentence,m+1,states[k])] / probabilityOfObservedSequence


        # #calculating deltas
        delta=dict()
        for m in range(1,len(setOfWords)+1): #For each word
            for j in range(0,len(states)):
                delta[(inputSentence),m,states[j]]=0
                if m!=6:
                    for k in range(0,len(states)):

                            delta[(inputSentence),m,states[j]]+=gamma[(inputSentence),m,states[j],states[k]]

                else:
                    delta[(inputSentence),m,states[j]]=alpha[(inputSentence,m,states[j])]/probabilityOfObservedSequence



        #Calculating next hidden markov model
        values=0
        print
        print "*" * 100
        print "Hidden markov model "+str(z+1)
        print "-" * 60

        #Calculate initial probabilities
        for i in range(0,4):

            values+=delta[(inputSentence,1,states[i])]
        initialProbabilitynew=dict()
        for i in range(0,4):
            print "Starting probability of state "+states[i]+" : "+str(delta[(inputSentence,1,states[i])]/values)
            initialProbabilitynew[states[i]]=delta[(inputSentence,1,states[i])]/values


        #Calculate new transition probabilites

        print
        dict1=dict()
        dict2=dict()
        for i in range(0,4):
            value1=0
            for j in range (0,4):

                value=0
                for k in range(1,len(setOfWords)):
                    value+=gamma[(inputSentence,k,states[i],states[j])]
                dict1[(states[i],states[j])]=value
                value1+=value
            dict2[states[i]]=value1
        transitionProbabilityDictionary.clear()
        for i in range(0,4):
            for j in range(0,4):
                transitionProbabilityDictionary[state1State2(state1=states[i], state2=states[j])]=dict1[(states[i],states[j])]/dict2[states[i]]
                print "Transition Probability from "+states[i]+" to "+states[j]+" : "+str(transitionProbabilityDictionary[state1State2(state1=states[i], state2=states[j])])

        #Calculate new emission probabilites
        print
        lexicalProbabilityDictionary.clear()

        for i in range(1,len(setOfWords)+1):

                for j in range(0,4):

                        k=delta[(inputSentence,i,states[j])]
                        l=0
                        for m in range(i+1,len(setOfWords)):
                            l+=delta[(inputSentence,m,states[j])]
                        if(setOfWords[i-1]!="a"):
                            lexicalProbabilityDictionary[wordPOSCombo(word=setOfWords[i-1], POS=states[j])] =k/(k+l)

                            print "Emmission probability of word \""+setOfWords[i-1]+"\" at state "+states[j]+" : "+str(lexicalProbabilityDictionary[wordPOSCombo(word=setOfWords[i-1], POS=states[j])])
        #Since the word "a" appears twice in the input sentence, we are handling it seperately below
        for i in range(0,4):

            lexicalProbabilityDictionary[wordPOSCombo(word='a', POS=states[i])] = (delta[(inputSentence,1,states[i])]+delta[(inputSentence,5,states[i])]) / (delta[(inputSentence,1,states[i])]+delta[(inputSentence,5,states[i])]+delta[(inputSentence,2,states[i])]+delta[(inputSentence,3,states[i])]+delta[(inputSentence,4,states[i])]+delta[(inputSentence,6,states[i])])
            print "Emmission probability of word a "+" at state "+states[i]+" : "+str(lexicalProbabilityDictionary[wordPOSCombo(word='a', POS=states[i])])


