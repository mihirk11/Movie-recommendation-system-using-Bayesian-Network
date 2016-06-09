import numpy as np
import pandas as pd
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel

data = pd.read_csv('~/Documents/unifiedMLData.csv')

#print data
movie_model = BayesianModel([
('occupation','rating')
#,('gender','rating')
#,('age','rating')
#,('age','occupation')
#,('gender','occupation')
#,('genre','movie_title')
#,('movie_title','rating')
                             ])
movie_model.fit(data)


model_infer = VariableElimination(movie_model)
results = model_infer.query('rating')

print(results['rating'])

#print(movie_model.get_cpds('rating'))