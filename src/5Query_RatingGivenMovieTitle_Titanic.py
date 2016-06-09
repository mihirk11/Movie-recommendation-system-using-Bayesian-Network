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



#Rating 1 Given movie is titanic
myquery = dict(rating=[1])
myevidence = dict(movie_title='Titanic (1997)')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result


tcf.refresh()

#Rating 2 Given movie is titanic
myquery = dict(rating=[2])
myevidence = dict(movie_title='Titanic (1997)')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()

#Rating 3 Given movie is titanic
myquery = dict(rating=[3])
myevidence = dict(movie_title='Titanic (1997)')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()

#Rating 4 Given movie is titanic
myquery = dict(rating=[4])
myevidence = dict(movie_title='Titanic (1997)')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()

#Rating 5 Given movie is titanic
myquery = dict(rating=[5])
myevidence = dict(movie_title='Titanic (1997)')
result=tcf.specificquery(query=myquery,evidence=myevidence)
print result

tcf.refresh()