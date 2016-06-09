from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
import numpy as np
import pandas as pd


#values = pd.DataFrame(np.random.randint(low=0, high=2, size=(1000, 5)),columns=['A', 'B', 'C', 'D', 'E'])

values1 = pd.read_csv('~/Documents/unifiedMLData.csv')
#print values1
values=pd.DataFrame(values1,columns=['movie_title', 'genre', 'age','occupation','rating','gender'])
#print values
s= values.reset_index().to_json(orient='records')
print s
#a= values.to_json()
#print a
#model = BayesianModel([('genre', 'movie_title'), ('age', 'occupation'),('occupation','rating'),('movie_title','rating')])
#model.fit(values)

#print model.get_cpds('genre')
#inference = VariableElimination(model)
#phi_query = inference.query(['age', 'occupation'])
#print(phi_query['occupation'])