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

#print json.dumps(result.randomsample(3), indent=2)
#print json.dumps(result.Vdata, indent=2)

print json.dumps(result, indent=2)

