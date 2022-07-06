
import numpy
import scipy.optimize
from RunProductionFn import *
import pickle
import json

def sumSquareError(params,inputData,outputData):
    fnOutput = RunProductionFn(inputData,params)
    return numpy.sum(numpy.square(outputData-fnOutput))

def TrainModel():

    dbfile = open('./data/interim/temp8', 'rb')
    InputData = pickle.load(dbfile)
    dbfile.close()
    dbfile = open('./data/interim/temp9', 'rb')
    OutputData = pickle.load(dbfile)
    dbfile.close()
    # initialize coefficients for optimization
    params = numpy.array([250.0,225.0,200.0,175.0,150.0,125.0,100.0,75.0,50.0,25.0,0.0, 10.0])

    res = scipy.optimize.minimize(sumSquareError,args = (InputData,OutputData),x0=params)

    error = sumSquareError(res.x,InputData,OutputData)

    dbfile = open('./models/DLmodel', 'ab')
    pickle.dump(res, dbfile)
    dbfile.close()

    dict = {
        "sum_sq_error" : error
    }        
    json_object = json.dumps(dict, indent = 4)

    with open("./reports/resultsmain.json", "w") as outfile:
        outfile.write(json_object)

    return

