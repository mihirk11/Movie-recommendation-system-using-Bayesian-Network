import json
import scipy as sp

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


text = open("../data/unifiedMLData2.json")
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

tcf=TableCPDFactorization(result)

#print "cpds"
#print tcf


myquery = dict(rating=[5])
myevidence = dict(occupation='student')

#print json.dumps(tcf.factorlist,indent=2)
#print json.dumps(tcf.condprobve(query=query1,evidence=evidence1),indent=2)

#res2=tcf.specificquery(query=query1,evidence=evidence1)
#res2=tcf.condprobve(query=query1,evidence=evidence1)
#res2=tcf.condprobve(query=myquery,evidence=myevidence)
res2=tcf.specificquery(query=myquery,evidence=myevidence)
#res2=tcf.specificquery(query=query1,evidence=evidence1)


print res2
#print json.dumps(res2.vals, indent=2)
#print json.dumps(res2.scope, indent=4)
#print json.dumps(res2.card, indent=6)
#print json.dumps(res2.stride, indent=8)
#print json.dumps(result.specificquery(query1,evidence1), indent=2)
