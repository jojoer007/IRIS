#predict.py
def load(path):
    import pickle
    infile = open(path,'rb')
    model = pickle.load(infile)
    infile.close()
    return model

#Main predict() function!
def predict(input_from_client):
    #1. import sklearn
    from sklearn.ensemble import RandomForestClassifier
    from numpy import array
    
    #2. load our model. We don't need load() function but it's nice to have. 
    model = load("model.pkl")
    
    #3. Once the model is loaded, feed the client's data into our model
    prediction = model.predict(input_from_client)
    value = []
    for label in prediction:
        if label == 0:
            value.append('Setosa')
        elif label == 1:
            value.append('Virginica')
        else:
            value.append('Versicolour')
    #4. Return prediction back to the client.
    return value