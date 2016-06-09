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


lgbn = LGBayesianNetwork(skel, nd)


text = open("../unifiedMLData2.json")
data=text.read()
printable = set(string.printable)


asciiData=filter(lambda x: x in printable, data)
listofDicts=json.loads(asciiData)



skel = GraphSkeleton()
skel.load("../skeleton.json")


learner = PGMLearner()


result = learner.discrete_mle_estimateparams(skel, listofDicts)


tcf=TableCPDFactorization(result)


myquery = dict(rating=[5])
myevidence = dict(occupation='student')
res2=tcf.gibbssample(evidence=myevidence,n=3)

print json.dumps(res2, indent=2)