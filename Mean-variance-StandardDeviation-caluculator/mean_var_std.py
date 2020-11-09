import numpy as np
from collections import OrderedDict 
calculations={}
def calculate(list):
    mat=np.reshape(list,(3,3))
    a=np.mean
    calculations['mean']=[a(mat,axis=1),a(mat,axis=0),[a(list)]]
    calculations['variance']=[np.var(mat,axis=1),np.var(mat,axis=0),[np.var(list)]]
    calculations['standard deviation']=[np.std(mat,axis=1),np.std(mat,axis=0),[np.std(list)]]
    calculations['max']=[np.max(mat,axis=1),np.max(mat,axis=0),[np.max(list)]]
    calculations['min']=[np.min(mat,axis=1),np.min(mat,axis=0),[np.min(list)]]
    calculations['sum']=[np.sum(mat,axis=1),np.sum(mat,axis=0),[np.sum(list)]]
    return calculations