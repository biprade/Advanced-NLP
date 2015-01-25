#Author : Bipra De
#Date : 20-Nov-2014

#PROBLEM STATEMENT

# Given, the grammar and rule potential values, implement CYK PARSING ALGORITHM to parse the given input string.

inputString="A dog ate pizza with a fork in a kitchen"
inputWords=inputString.split(" ")

#preparing rules dictionary
grammar=dict()
grammar['NP','VP']='S'
grammar['DET','N']='NP'
grammar['N']='NP'
grammar['NP','PP',1]='NP'
grammar['V','NP']='VP'
grammar['V','XP']='VP'
grammar['IN','NP']='PP'
grammar['NP','PP',2]='XP'
grammar['a']='DET'
grammar['A']='DET'
grammar['dog']='N'
grammar['pizza']='N'
grammar['fork']='N'
grammar['kitchen']='N'
grammar['ate']='V'
grammar['with']='IN'
grammar['in']='IN'

#preparing rule potentials
rulePotential=dict()
rulePotential['S','NP','VP']=1.0
rulePotential['NP','DET','N']=0.4
rulePotential['NP','N']=0.3
rulePotential['NP','NP','PP']=0.3
rulePotential['VP','V','NP']=0.8
rulePotential['VP','V','XP']=0.2
rulePotential['PP','IN','NP']=1.0
rulePotential['XP','NP','PP']=1.0
rulePotential['DET','a']=1.0
rulePotential['DET','A']=1.0
rulePotential['N','dog']=0.1
rulePotential['N','pizza']=0.2
rulePotential['N','fork']=0.4
rulePotential['N','kitchen']=0.3
rulePotential['V','ate']=1.0
rulePotential['IN','with']=0.4
rulePotential['IN','in']=0.6

#Stores all the values of a particular row in the CYK Parser chart
cykRow=[dict() for x in range(10)]

#Represents the CYK Parser chart
cykChart=[[dict() for x in range(10)] for x in range(11)]

#Preparing the level 0 of the Chart i.e. ['A', 'dog', 'ate', 'pizza', 'with', 'a', 'fork', 'in', 'a', 'kitchen']
for i in range(0,len(inputWords)):

    #Adding all the  words of the input sentence to level 0 of the CYK chart
    cykRow[i]=inputWords[i]

cykChart[0]=cykRow


#Preparing level 1 of the chart from the given grammar with all the terminal rules
cykRow=[dict() for x in range(10)]
for j in range(0,len(inputWords)):

     rule=dict()
     chartValue=dict()
     rule[grammar[inputWords[j]]]=inputWords[j]

     #Adding NP from the  rule NP->N for all occurrences of N at level 1
     if grammar[inputWords[j]]=='N':
         rule['NP']='N'
         chartValue['inside prob rooted at NP']=rulePotential['NP','N']*rulePotential['N',inputWords[j]]


     chartValue['Rules']=rule
     chartValue['inside prob rooted at '+grammar[inputWords[j]]]=rulePotential[grammar[inputWords[j]],inputWords[j]]

     cykRow[j]=chartValue

#Adding the terminal rules and their inside probabilities to level 1 of the CYK chart
cykChart[1]=cykRow

# Preparing level 2 to level 10 of the CYK Parser Chart

# Outermost loop "i" iterates over all the levels of the CYK chart from level 2 to level 10
for i in range(2,len(inputWords)+1):

    cykRow=[dict() for x in range(10)]

    #This loop "j" iterates over the row elements of the CYK Parser chart
    for j in range(0,len(inputWords)):

         insideProbability=0

         # This loop "k" iterates over the already populated levels of the CYK chart i.e for a given level i, it iterates
         # over all the levels from level i-1 to level 1 to parse the relevant rules
         for k in range(i-1,0,-1):

            rule=dict()
            chartValue=dict()

            if i>2 and k>1:
                if j+k<=len(inputWords)-1:
                    if cykChart[k][j]:

                        if cykChart[i-k][j+k]:
                            leftChild=cykChart[k][j]
                            rightChild=cykChart[i-k][j+k]

                            leftChildNode=leftChild.get('Rules').keys()
                            rightChildNode=rightChild.get('Rules').keys()


                            for lnode in leftChildNode:
                                for rnode in rightChildNode:

                                    #This conditional construct handles the ambiguous grammar : NP->NP,PP and XP->NP,PP
                                    if lnode=="NP" and rnode=="PP":
                                        check1=(lnode,rnode,1)
                                        check2=(lnode,rnode,2)
                                        if check1 in grammar.keys() and check2 in grammar.keys():
                                            chartValue['inside prob rooted at NP']=(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-k][j+k].get('inside prob rooted at '+rnode))*rulePotential[grammar[check1],lnode,rnode]
                                            chartValue['inside prob rooted at XP']=(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-k][j+k].get('inside prob rooted at '+rnode))*rulePotential[grammar[check2],lnode,rnode]
                                            rule[grammar[check1]]=(str(check1).replace(", 1",""))
                                            rule[grammar[check2]]=(str(check2).replace(", 2",""))
                                    else:
                                        check=(lnode,rnode)
                                        #Checking if the  rule exists in the grammar list
                                        if check  in grammar.keys():

                                            insideProbability=insideProbability+(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-k][j+k].get('inside prob rooted at '+rnode))*rulePotential[grammar[check],lnode,rnode]

                                            # This conditional construct handles cases of ambiguity like VP->V,NP and VP->V,XP
                                            if (grammar[check] not in rule.keys()):
                                                rule[grammar[check]]=check
                                            else:
                                                rule[grammar[check]]=rule[grammar[check]]+(lnode,rnode)

                                            chartValue['inside prob rooted at '+grammar[check]]=insideProbability


            if i>2 and k==1:
                if j+1<len(inputWords):

                    if cykChart[k][j]:
                        #print "Hello"
                        if cykChart[i-1][j+1]:
                            leftChild=cykChart[k][j]
                            rightChild=cykChart[i-1][j+1]

                            leftChildNode=leftChild.get('Rules').keys()
                            rightChildNode=rightChild.get('Rules').keys()

                            for lnode in leftChildNode:
                                for rnode in rightChildNode:

                                     #This conditional construct handles the ambiguous grammar : NP->NP,PP and XP->NP,PP
                                    if lnode=="NP" and rnode=="PP":
                                        check1=(lnode,rnode,1)
                                        check2=(lnode,rnode,2)
                                        if check1 in grammar.keys() and check2 in grammar.keys():
                                            chartValue['inside prob rooted at NP']=(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-1][j+1].get('inside prob rooted at '+rnode))*rulePotential[grammar[check1],lnode,rnode]
                                            insideProbabilityNP=(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-1][j+1].get('inside prob rooted at '+rnode))*rulePotential[grammar[check1],lnode,rnode]
                                            chartValue['inside prob rooted at XP']=(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-1][j+1].get('inside prob rooted at '+rnode))*rulePotential[grammar[check2],lnode,rnode]
                                            insideProbabilityXP=(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-1][j+1].get('inside prob rooted at '+rnode))*rulePotential[grammar[check2],lnode,rnode]
                                            rule[grammar[check1]]=(str(check1).replace(", 1",""))
                                            rule[grammar[check2]]=(str(check2).replace(", 2",""))

                                    else:
                                        check=(lnode,rnode)
                                        #Checking if the  rule exists in the grammar list
                                        if check  in grammar.keys():
                                            insideProbability=insideProbability+(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[i-1][j+1].get('inside prob rooted at '+rnode))*rulePotential[grammar[check],lnode,rnode]

                                            # This conditional construct handles cases of ambiguity like VP->V,NP and VP->V,XP
                                            if (grammar[check] not in rule.keys()):
                                                rule[grammar[check]]=check
                                            else:
                                                rule[grammar[check]]=rule[grammar[check]]+(lnode,rnode)


                                            chartValue['inside prob rooted at '+grammar[check]]=insideProbability




            #This conditional construct has logic to prepare level 2 of the CYK Chart
            if i==2:
                if j+1<len(inputWords):

                    if cykChart[k][j]:

                        if cykChart[k][j+k]:
                            leftChild=cykChart[k][j]
                            rightChild=cykChart[k][j+k]

                            leftChildNode=leftChild.get('Rules').keys()
                            rightChildNode=rightChild.get('Rules').keys()


                            for lnode in leftChildNode:
                                for rnode in rightChildNode:
                                    check=(lnode,rnode)

                                    if check  in grammar.keys():

                                        insideProbability=(cykChart[k][j].get('inside prob rooted at '+lnode))*(cykChart[k][j+k].get('inside prob rooted at '+rnode))*rulePotential[grammar[check],lnode,rnode]
                                        if (grammar[check] not in rule.keys()):
                                                rule[grammar[check]]=check
                                        else:
                                                rule[grammar[check]]=rule[grammar[check]]+(lnode,rnode)

                                        chartValue['inside prob rooted at '+grammar[check]]=insideProbability

            if(bool(rule)):
                    chartValue['Rules']=rule
                    #This conditional construct handles the ambiguous grammar : NP->NP,PP and XP->NP,PP
                    if (bool(cykRow[j].get('Rules'))):

                        if rule.keys()==cykRow[j].get('Rules').keys():

                            rules=str(cykRow[j].get("Rules").keys()).replace("[","").replace("]","").replace("'","").replace(" ","").split(",")

                            for rule in rules:

                                if rule=='NP':
                                    insideProb=cykRow[j].get('inside prob rooted at '+rule)

                                    insideProb=insideProb+insideProbabilityNP

                                    cykRow[j]['inside prob rooted at NP']=insideProb

                                elif rule=='XP':
                                    insideProb=cykRow[j].get('inside prob rooted at '+rule)


                                    insideProb=insideProb+insideProbabilityXP

                                    cykRow[j]['inside prob rooted at XP']=insideProb

                    else:
                            cykRow[j]=chartValue
                            cykChart[i]=cykRow

print "Find below the CYK Parse chart which is a 11 *10 matrix"
print "Blank cells in the CYK Parse chart are denoted by {}"
print
for i in range(0,11):
    print "Level "+str(i)
    print cykChart[i]
    print






















