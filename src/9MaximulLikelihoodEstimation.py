import json
import sys
import string

from libpgm.nodedata import NodeData
from libpgm.graphskeleton import GraphSkeleton
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.lgbayesiannetwork import LGBayesianNetwork
from libpgm.hybayesiannetwork import HyBayesianNetwork
from libpgm.dyndiscbayesiannetwork import DynDiscBayesianNetwork
from libpgm.tablecpdfactorization import TableCPDFactorization
from libpgm.sampleaggregator import SampleAggregator
from libpgm.pgmlearner import PGMLearner




text = open("../unifiedMLData2.json")
data=text.read()
printable = set(string.printable)
asciiData=filter(lambda x: x in printable, data)
#print asciiData


#listofDicts=json.dumps(data)
listofDicts=json.loads(asciiData)
#print listofDicts[0]

skel = GraphSkeleton()
skel.load("../skeleton.json")

learner = PGMLearner()

result = learner.discrete_mle_estimateparams(skel, listofDicts)



#print json.dumps(result.randomsample(10), indent=2)
#print json.dumps(result.Vdata, indent=2)





#nd = NodeData()
#nd.load("../tests/unittestdict.txt")



#evidence = dict(Letter='weak')
tcf=TableCPDFactorization(result)




occupations = ['administrator',
'artist'
'doctor'
'educator'
'engineer'
'entertainment'
'executive'
'healthcare'
'homemaker'
'lawyer'
'librarian'
'marketing'
'none'
'other'
'programmer'
'retired'
'salesman'
'scientist'
'student'
'technician'
'writer']

myevidence = dict(gender='F')
res2 = []
for occu in occupations:
    myquery = dict(occupation=[occu])
    res2=tcf.condprobve(query=myquery,evidence=myevidence)
    #res2=tcf.specificquery(query=myquery,evidence=myevidence)
    #print res2
    print json.dumps(res2.vals, indent=2)
mle = res2[0]
for i in range(1,len(res2)-1):
    mle = max(res2[i-1],res2[i])
print "mle of occupation given gender is Female"
print mle