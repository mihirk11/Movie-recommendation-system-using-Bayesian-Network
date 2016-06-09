import json
import sys
import string

from libpgm.graphskeleton import GraphSkeleton
from libpgm.tablecpdfactorization import TableCPDFactorization
from libpgm.pgmlearner import PGMLearner

text = open("../unifiedMLData2.json")
data=text.read()
printable = set(string.printable)
asciiData=filter(lambda x: x in printable, data)


#listofDicts=json.dumps(data)
listofDicts=json.loads(asciiData)

skel = GraphSkeleton()
skel.load("../skeleton.json")

learner = PGMLearner()

result = learner.discrete_mle_estimateparams(skel, listofDicts)

tcf=TableCPDFactorization(result)



#Rating 1 Given Occupation is student
myquery = dict(rating=[1])
myevidence = dict(occupation='student')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result


tcf.refresh()

#Rating 2 Given Occupation is student
myquery = dict(rating=[2])
myevidence = dict(occupation='student')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()

#Rating 3 Given Occupation is student
myquery = dict(rating=[3])
myevidence = dict(occupation='student')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()

#Rating 4 Given Occupation is student
myquery = dict(rating=[4])
myevidence = dict(occupation='student')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()

#Rating 5 Given Occupation is student
myquery = dict(rating=[5])
myevidence = dict(occupation='student')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()