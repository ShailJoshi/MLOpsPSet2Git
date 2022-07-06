import numpy
#from CleanUpDf import *
#from FeatureArrays import *

from RunProductionFn import *
#from TrainModel import *
import pickle

#CleanUpDf()
#FeatureArrays()
#TrainModel()


dbfile = open('./models/DLmodel', 'rb')
Model = pickle.load(dbfile)
dbfile.close()
print("Enter number of overs remaining\n")
num1 = int(input())
print("Enter number of wickets gone\n")
num2 = int(input())

query = numpy.array([num1,num2])

RemResource = RunProductionFn(query,Model.x)

NormFact = RunProductionFn(numpy.array([50,0]),Model.x)
print("\nBatting side resources remaining in percentage:\n")
print(RemResource/NormFact*100)
#print(RemResource)