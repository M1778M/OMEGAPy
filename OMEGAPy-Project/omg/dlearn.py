import numpy as np
import random
from .tools.listTool import srange

# Basic Data Machine Learning Library for seeing how it works with simple learners
# Easy and Fast to use 
# The Performance of this module isn't good it's just for learning how a machine learning algorithm makes

_STD_ITER_FOR_LOOP = 100
class Model: # Models in dlearn are for fitting data and predict X
    def __init__(self,model_dlearner):
        self.model_name = None
        self.version = 1.0
        self._dlearner_func=model_dlearner # _dlearner_func is a function that learns by X and y for prediction
        self.weights = [] # weights they are a number uses for predict X
    def fit(self,X,y):
        ...
    def predict(self,x):
        ...
    def __repr__(self):
        return f"<Model '{self.model_name}' version={self.version}>"
class Layer:
    def __init__(self,func):
        self._main_func = func
    def __call__(self,*args):
        return self._main_func(*args)

def _dlminLoss_trainingloop_01(X,y,iter_,weight=None,step=0.01,weight_calc=0.001):
    wisn = weight
    last_out = [0,100000]
    for _ in srange(int(-iter_),int(iter_),step=step):
        if wisn == None:
            weight = _
            output = list(_datalearner_01(X,y,_STD_ITER_FOR_LOOP,weight,weight_calc))
            if output[1] >= last_out[1]:
                continue
            else:
                last_out = output
    return last_out
        
def _datalearner_01(X,y,iter_=1000,weight=None,weight_calc=0.001):
    if weight == None:
        weight=np.random.randn()
    operations = ['add','sub']
    operation = random.choice(operations)
    weight_calc=weight_calc
    last_loss = 1000000
    for _ in range(iter_):
        for i in range(len(X)):
            if operation == 'add':
                yhat=0
                for j in range(len(X[i])):
                    yhat += X[i][j]*weight
                    loss = (y[i]-yhat)**2
                    if loss > last_loss:
                        last_loss = loss
                        operation = 'sub'
                        continue
                    last_loss = loss
                    weight+=weight_calc
            elif operation == 'sub':
                yhat=0
                for j in range(len(X[i])):
                    yhat = X[i][j]*weight
                    loss = (y[i]-yhat)**2
                    if loss > last_loss:
                        last_loss = loss
                        operation = 'add'
                        continue
                    last_loss = loss
                    weight-=weight_calc
    return weight,last_loss

def _SimpleNN_01 (*data):
    def _layer1_func(*x):
        _ = ([])
        e=(255,255,255)
        k=[255,6,1]
        for i in x:
            for j in range(10000):
                i+=-1*random.choice(k) if (sum(e)-j)>=sum(e) else j*random.choice(k)
            _.append(i)
        return _
    def _layer2_func(*x):
        _ = ([])
        formula = 'Xi/2-Xi**2'
        for i in x:
            _.append(i/2-i**2)
        return _
    def _layer3_func(*x):
        _ = ([])
        for i in x:
            _.append((i**2)/abs(i))
        return _
    def _layer4_func(*x):
        _ = ([])
        for i in x:
            for i in range(200000):
                i-=random.randint(0,i)
            _.append(i/2)
        return _

    Layer1= Layer(_layer1_func)
    Layer2= Layer(_layer2_func)
    Layer3= Layer(_layer3_func)
    Layer4= Layer(_layer4_func)
    return Layer4(*Layer3(*Layer2(*Layer1(*data))))

def dlpredict_(model,X):
    return model.predict(X)

class SimpleDL_01(Model):
    def __init__(self,iter_=1000,step=50):
        self.iter_ = iter_
        self._step = step
        super().__init__(_dlminLoss_trainingloop_01)
        self.model_name = 'SimpleDL_01'
        self.version=1.1
    def advfit(self,X,y,weight=None,weight_calc=None):
        self.weights = []
        if not weight_calc:
            for i in range(0,len(X[0])):
                self.weights.append(self._dlearner_func([X[:,i]],y,self.iter_,step=self._step,weight=weight))
            return self
        for i in range(0,len(X[0])):
            self.weights.append(self._dlearner_func([X[:,i]],y,self.iter_,step=self._step,weight=weight,weight_calc=weight_calc))
        return self
    
    def fit(self,X,y):
        self.weights = []
        for i in range(0,len(X[0])):
            self.weights.append(self._dlearner_func([X[:,i]],y,self.iter_,step=self._step))
        return self
    def predict(self,x):
        sum = 0
        for i in range(len(self.weights)):
            sum+=self.weights[i]*x[i]
        return sum
