from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
import math
def model():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt('Data/train.csv', delimiter=',', dtype='f8')[1:]    
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt('Data/test.csv', delimiter=',', dtype='f8')[1:]

    #create and train the random forest
    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train, target)
    predicted_probs = [[index + 1, x[1]] for index, x in enumerate(rf.predict_proba(test))]

    savetxt('Data/submission.csv', predicted_probs, delimiter=',', fmt='%d,%f', 
            header='MoleculeId,PredictedProbability', comments = '')

import scipy as sp
def llfun(act, pred):
    epsilon = 1e-15
    pred = sp.maximum(epsilon, pred)
    pred = sp.minimum(1-epsilon, pred)
    ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
    ll = ll * -1.0/len(act)
    return ll

from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
import numpy as np
def get_data():
    #read in  data, parse into training and target sets
    dataset = np.genfromtxt('Data/train.csv', delimiter=',', dtype='f8')[1:]    
    target = np.array([x[0] for x in dataset])
    train = np.array([x[1:] for x in dataset])

    #In this case we'll use a random forest, but this could be any classifier
    #cfr = RandomForestClassifier(n_estimators=100)

    #Simple K-Fold cross validation. 5 folds.
    #(Note: in older scikit-learn versions the "n_folds" argument is named "k".)
    #cv = cross_validation.KFold(len(train), n_folds=5, indices=False)

    #iterate through the training and test cross validation segments and
    #run the classifier on each one, aggregating the results into a list
    results = []
    #for traincv, testcv in cv:
    #            probas = cfr.fit(train[traincv], target[traincv]).predict_proba(train[testcv])
    #            results.append(llfun(target[testcv], [x[1] for x in probas]))

    #print out the mean of the cross-validated results
    #print ("Results: " + str( np.array(results).mean()))
def logistic_reg(train, target):
    Theta = [0 for i in range(len(train[0]) + 1)]
    for i in range(0, 5000):
        d = derivative(train, target,Theta) 
        Theta = np.subtract(Theta, d)
        #print(Theta, d)
    print('d is', d)
    return Theta
def sigmoid(z):
    return 1 / (1 + math.exp(z * -1))
def add_col(train):
    col1 = [[1 for j in range(1)]
               for i in range(len(train))]
    return np.append(col1,train,1)

def z(Theta,train):
    train1 = add_col(train)
    return np.dot(train1, Theta)

def derivative(train, target,Theta):
    zz = z(Theta,train)
    #print(len(zz))
    #h = [sigmoid(i) for i in zz]
    #print(len(h))
    #diff = np.subtract(h,target)
    diff = [sigmoid(j) - target[i] for i,j in enumerate(zz)]
    train1 = add_col(train)
    result = np.dot(np.transpose(train1),diff)
    #print(len(result))
    return result / len(train)


dataset = np.genfromtxt('Data/train.csv', delimiter=',', dtype='f8')[1:]    
train = np.array([x[1:] for x in dataset])
target = np.array([x[0] for x in dataset])
test = np.genfromtxt('Data/test.csv', delimiter=',', dtype='f8')[1:]
cv = cross_validation.KFold(len(dataset), n_folds=5, indices=False)
print("cv =", cv)
results = []
for traincv, testcv in cv:
    print("len traincv =", len(traincv), "len testcv =", len(testcv))
    print("traincv =", traincv, "testcv =", testcv)
    result_theta = logistic_reg(train[traincv],target[traincv])
    zz = z(result_theta, train[testcv])
    sig = [sigmoid(i) for i in zz]
    #print(sig)
    results.append(llfun(target[testcv], sig))

    #print out the mean of the cross-validated results
print ("Results: " + str( np.array(results).mean()))

#if __name__=="__main__":
    #for traincv, testcv in cv:
#    main()
