import numpy as np
import math
import pandas as pd
import scipy as sp
from sklearn import cross_validation
def logistic_reg(train, target):
    Theta = [0 for i in range(len(train[0]) + 1)]
    #print('Theta',len(Theta))
    for i in range(0, 30000):
        d = derivative(train, target,Theta) * 0.006 
        Theta = np.subtract(Theta, d)
        #print(Theta, d)
    print('d is', d)
    return Theta
def sigmoid(z):
    return 1 / (1 + np.exp(z * -1))
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
def predict(Theta,test):
    zz = z(Theta, test)
    sig = [1 if sigmoid(i) >= 0.5 else 0 for i in zz]
    return sig
def sex_convert(sex):
    return 1 if sex == "male" else 0
def embark_convert(embark):
    if (embark == 'S'):
        return 1
    elif (embark == 'C'):
        return 2
    elif (embark == 'Q'):
        return 3
    else:
        return 0
# dataset = np.genfromtxt('Titanic/train.csv', delimiter=',', dtype='f8')[1:]    
dataset = pd.read_csv("Titanic/train.csv", usecols = [0,1,2,4,5,6,7,9,11],converters={"Sex":sex_convert,"Embarked":embark_convert})
#dataset = pd.read_csv("Titanic/train.csv", usecols = [0,1,2,4],converters={"Sex":sex_convert})
#dataset = pd.read_csv("Titanic/train.csv", quotechar='"')
train = np.array([x[2:] for x in dataset.fillna(0).values])
target = np.array([x[1] for x in dataset.fillna(0).values])
# test = np.genfromtxt('Titanic/test.csv', delimiter=',', dtype='f8')[1:]
#test = pd.read_csv("Titanic/test.csv", quotechar='"')
testset = pd.read_csv("Titanic/test.csv", usecols = [0,1,3,4,5,6,8,10],converters={"Sex":sex_convert,"Embarked":embark_convert}).fillna(0)
#testset = pd.read_csv("Titanic/test.csv", usecols = [0,1,3],converters={"Sex":sex_convert}).fillna(0)
test = np.array([x[1:] for x in testset.values])
ids = np.array([x[0] for x in testset.values])
cv = cross_validation.KFold(len(dataset), n_folds=5, indices=False)
results = []
for traincv, testcv in cv:
    result_theta = logistic_reg(train[traincv],target[traincv])
    #print(sig)
    sig = predict(result_theta,train[testcv])
    count = 0
    for i, _ in enumerate(sig):
        if sig[i] == target[testcv][i]:
            count += 1
    results.append(count / len(train[testcv]))

    #print out the mean of the cross-validated results
print ("Results: " + str( np.array(results).mean()))
print(results)
result_theta = logistic_reg(train,target)
sig = predict(result_theta,test)
#print(len(ids),len(sig))
#print(np.append(ids,sig,1))
result_array = [[ids[i],sig[i]] for i,_ in enumerate(ids)]
np.savetxt('Titanic/submission.csv', result_array, delimiter=',', fmt='%d,%d', 
                        header='PassengerId,Survived', comments = '')
#pd.write_csv("Titanic\submission.csv",np.append(ids,sig,1))
#if __name__=="__main__":
    #for traincv, testcv in cv:
#    main()
