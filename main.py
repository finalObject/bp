#!/usr/local/bin/python3
from nnl import *

layerSize=[2]
rate=1
x=Symbol('x')
activateFunction=1/(1+rate*math.e**(-x))
updateRate=1
trainData=[[1,1,1,1,1,2],]
nw = NeuralNetwork(layerSize,activateFunction,updateRate,trainData)