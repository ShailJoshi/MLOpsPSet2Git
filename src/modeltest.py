import numpy
import sys
sys.path.insert(0, './src/models/')
from RunProductionFn import *
import pickle

def test1():
    dbfile = open('./models/DLmodel', 'rb')
    Model = pickle.load(dbfile)
    dbfile.close()
    assert 230.<=RunProductionFn(numpy.array([50,0]),Model.x)<=280.

def test2():
    dbfile = open('./models/DLmodel', 'rb')
    Model = pickle.load(dbfile)
    dbfile.close()
    assert 0.01> RunProductionFn(numpy.array([0,0]),Model.x)

def test3():
    dbfile = open('./models/DLmodel', 'rb')
    Model = pickle.load(dbfile)
    dbfile.close()
    assert 0.01> RunProductionFn(numpy.array([50,10]),Model.x)