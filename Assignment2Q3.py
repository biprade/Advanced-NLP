#Author : Bipra De
#Date : 25-Sep-2014

#PROBLEM STATEMENT

# (a) Write a program that extracts trigrams from a text.
#     The trigrams should be based on sentences, i.e. you have to assume sentence-beginning and -end markers.
#     The text will have one sentence per line. Punctuation is split off. Run the n-gram extraction on the files hw2-train.txt and hw2-test.txt.
# (b) Calculate the trigram perplexity of text hw2-test.txt given hw2-train.txt.

from __future__ import division
import re

##################################################################################################
#VARIABLES                                       USAGE
#trigramsDictionary                              Stores trigrams of the training set and their count
#bigramsDictionary                               Store bigrams of the training set and their count
#trigramProbabilityDistribution                  Store the trigrams in the training set and their probability
#trigramsDictionaryTestSample                    Store the trigrams of the test set and their count
#noOfWordsInTestFile                             Store the number of words in the test file to be used in perplexity formula
#probabiltyOfTestSet                             Stores the inverse of the joint probability of the test set using trigrams
#NOTE : Assumed the probability of the missing trigrams in the test set as 0.001
##################################################################################################
#data structures
trigramsDictionary=dict()                        #to store all trigrams in the training set
bigramsDictionary=dict()                         #to store all bigrams in the training set
trigramProbabilityDistribution=dict()            #to store the trigrams and their probability distribution
##################################################################################################

lines=tuple(open("/Users/biprade/Documents/B659 Advanced NLP/Assignment 2/hw2-train.txt","r")) #open the training set

for line in lines:                                      #reading the training file line by line
    inputString=re.sub('[\n.!,;?"-]', '', line)         #replace the listed punctuations with blank
    inputString=re.sub('n\'t',' not',inputString)       #split words like couldn't to could not
    inputString="START START "+inputString+"END"        #Adding START and END keywords as delimiters to mark the beginning and end of a sentence
    words=inputString.lower().split()                   #split the input string into words

    for i in range(0,len(words)-2):                     #preparing the trigram dictionary with their count
        trigram=words[i]+" "+words[i+1]+" "+words[i+2]
        if trigram in trigramsDictionary:
            trigramsDictionary[trigram]+=1
        else:
            trigramsDictionary[trigram]=1

    for i in range(0,len(words)-1):                    #preparing the bigram dictionary with their count
        bigram=words[i]+" "+words[i+1]
        if bigram in bigramsDictionary:
            bigramsDictionary[bigram]+=1
        else:
            bigramsDictionary[bigram]=1


for trigram in trigramsDictionary:                     #preparing the trigram dictionary with the probability of each trigram
        wordList=trigram.split()
        words=wordList[0]+" "+wordList[1]
        trigramProbabilityDistribution[trigram]=trigramsDictionary[trigram]/bigramsDictionary[words]

#Reading the training set and calculating the trigram distribution is now complete

#######################################################################################################################

#Now reading the test file and calculate the perplexity
lines=tuple(open("/Users/biprade/Documents/B659 Advanced NLP/Assignment 2/hw2-test.txt","r"))   #open test file
trigramsDictionaryTestSample=list()
noOfWordsInTestFile=0
for line in lines:                                              #read the test file line by line
    inputString=re.sub('[\n.!,;?"-]', '', line)                 #replace the listed punctuations with blank
    inputString=re.sub('n\'t',' not',inputString)               #split the words like couldn't to could not
    inputString="START START "+inputString+"END"                #Adding START and END keywords as delimiters to mark the beginning and end of a sentence
    words=inputString.lower().split()                           #split the string into words
    noOfWordsInTestFile=noOfWordsInTestFile+len(words)-2        #calculating the total no of words in a sentence excluding the 2 START sentence identifiers to calculate perplexity

    for i in range(0,len(words)-2):                             #preparing the trigram list in the test set
        trigram=words[i]+" "+words[i+1]+" "+words[i+2]
        trigramsDictionaryTestSample.append(trigram)

probabilityOfTestSet=1
print
for trigramTest in trigramsDictionaryTestSample:                #calculating the inverse of joint probability of the test set

   if trigramTest in trigramProbabilityDistribution:
       probabilityOfTestSet=probabilityOfTestSet * (1/ trigramProbabilityDistribution[trigramTest])
   else:
       probabilityOfTestSet=probabilityOfTestSet * (1/0.001)

print
print
print "Perplexity of the test set using trigrams from the training set is : "
print
print probabilityOfTestSet ** (1/(noOfWordsInTestFile))           #perplexity formula in use
print
print "Trigram probability distribution in the Training set in the form of {trigram:probability}:"
print "-" *88
for key in trigramProbabilityDistribution:                        #printing the trigram probability distribution from the training set
    print "{"+key+" : "+str(trigramProbabilityDistribution[key])+"}"









