
import numpy
import scipy.optimize
from RunProductionFn import *
import pickle

def sumSquareError(params,inputData,outputData):
    fnOutput = RunProductionFn(inputData,params)
    return numpy.sum(numpy.square(outputData-fnOutput))

def TrainModel():

    dbfile = open('./data/interim/temp2', 'rb')
    InputData = pickle.load(dbfile)
    dbfile.close()
    dbfile = open('./data/interim/temp3', 'rb')
    OutputData = pickle.load(dbfile)
    dbfile.close()
    # initialize coefficients for optimization
    params = numpy.array([250.0,225.0,200.0,175.0,150.0,125.0,100.0,75.0,50.0,25.0,0.0, 10.0])

    res = scipy.optimize.minimize(sumSquareError,args = (InputData,OutputData),x0=params)

    dbfile = open('./models/DLmodel', 'ab')
    pickle.dump(res, dbfile)
    dbfile.close()
    return 1

