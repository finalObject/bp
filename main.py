#!/usr/local/bin/python3
from nnl import *

layerSize=[3,2]
rate=1
x=Symbol('x')
activateFunction=1/(1+rate*math.e**(-x))
updateRate=1
trainData=[[1,1,1,1,1,2],]
nw = NeuralNetwork(layerSize,activateFunction,updateRate,trainData)
out1 = nw.getOutput(0)
print(out1)