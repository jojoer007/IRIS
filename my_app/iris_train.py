#Train the Model
from sklearn import linear_model, datasets
from sklearn import datasets
import numpy as np
import pickle


iris = datasets.load_iris()
X = iris.data[:, :] 
Y = iris.target
model = linear_model.LogisticRegression(C=1e5)
model.fit(X,Y)

#Once the model is trained, save it using pickle.
filename = 'model.pkl'
outfile = open(filename,'wb')
pickle.dump(model,outfile)
outfile.close()

#Load the model back, just to make sure everything is good!
infile = open(filename,'rb')
model = pickle.load(infile)
infile.close()
model