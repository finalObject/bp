
import random
import math
from sympy import *
#There are two types in Neuron.
#One is in input layer which getOutput is constant
#The other is in hidden layer which getOutput is var
class Neuron:
	def __init__(self,weights=[],bias=[],value=-2):
		self.weights=weights
		self.bias=bias
		self.value=value
	def getValue(self):
		return self.value
	#function for hidden layer neuron.
	def updateValue(self,inputSum,activateFunction):
		if self.weights == []:
			print('it is a neuron in input layer!Can not update')
			return 
		self.value = float(activateFunction.subs(Symbol('x'),inputSum))
		return self.value
	def getInputSum(self,upperLayer):
		if self.weights == []:
			print('it is a neuron in input layer!No Input sum')
			return []
		inputSum=0.0
		for index in range(0,len(upperLayer.neurons)):
			inputSum = inputSum+upperLayer.neurons[index].getValue()*self.weights[index]
		inputSum=inputSum+self.bias
		return inputSum
	def display(self):
		if self.weights == []:
			print('Neuron in Input layer,value=%f'%(self.value))
		else:
			print('Neuron in hidden layer,weights=%s,bias=%f'%(self.weights,self.bias))
		return
class NeuronLayer:
	def __init__(self,neurons=[]):
		self.neurons=neurons
	def display(self):
		print('In this layer:')
		for neuron in self.neurons:
			print('\t',end='')
			neuron.display()

class NeuralNetwork:
	inputLayer=[]
	hiddenLayers=[]
	outputNeuron=Neuron([],[])
	def __init__(self,layerSize,activateFunction,updateRate,trainData):
		#layerSize [1,2] means first layer has one neuron,second layer has two neuron
		self.layerSize = layerSize
		self.activateFunction = activateFunction
		self.updateRate = updateRate
		self.trainData = trainData
		#init hiddenLayer
		for i in range(len(self.layerSize)):
			tmpNS = []
			for j in range(self.layerSize[i]):
				tmpNS.append(Neuron([],[]))
			self.hiddenLayers.append(NeuronLayer(tmpNS))
	#good
	def calculateInputLayer(self,index):
		tmpNS=[];
		for i in range(len(self.trainData[index])-1):
			tmpNS.append(Neuron([],[],self.trainData[index][i]))
		self.inputLayer=NeuronLayer(tmpNS)
	def calculateHiddenLayers(self):
		for i in range(len(self.layerSize)):
			if i==0:
				upperLayer=self.inputLayer
			else:
				upperLayer=self.hiddenLayers[i-1]
			for j in range(self.layerSize[i]):
				tmpNS = self.hiddenLayers[i].neurons[j]			
				#init weights
				if tmpNS.weights==[]:
					tmpNS.weights=[1/len(upperLayer.neurons) for x in len(upperLayer.neurons)]
				inputSum = tmpNS.getInputSum(upperLayer)
				tmpNS.updateValue(inputSum,self.activateFunction)
	def calculateOutputNeuron():
		upperLayer = self.hiddenLayers[-1]
		#init weights
		if self.outputNeuron.weights==[]:
			self.outputNeuron.weights=[1/len(upperLayer.neurons) for x in len(upperLayer.neurons)]
		inputSum = self.outputNeuron.getInputSum(upperLayer)
		self.outputNeuron.updateValue(inputSum,self.activateFunction)
	def getOutput(self,index):
		calculateInputLayer(index)
		calculateHiddenLayers()
		calculateOutputNeuron()
		return self.outputNeuron.value		
		


















		


