from cgi import test
import numpy
from RunProductionFn import *
import pickle

def pytest1():
    dbfile = open('./models/DLmodel', 'rb')
    Model = pickle.load(dbfile)
    dbfile.close()
    assert 230.<=RunProductionFn(numpy.array([50,0]),Model.x)<=280.

def pytest2():
    dbfile = open('./models/DLmodel', 'rb')
    Model = pickle.load(dbfile)
    dbfile.close()
    assert 0.01> RunProductionFn(numpy.array([0,0]),Model.x)

def pytest3():
    dbfile = open('./models/DLmodel', 'rb')
    Model = pickle.load(dbfile)
    dbfile.close()
    assert 0.01> RunProductionFn(numpy.array([50,10]),Model.x)


print("Running test 1")
pytest1()
print("Running test 2")
pytest2()
print("Running test 3")
pytest3()
