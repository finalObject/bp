
import random
import math
from sympy import *
#bias [-1,1]
#weights [-1,1]
#activateFunction 1/(1+rate*math.e**(-x))
#input range [0,1]

#There are two types in Neuron.
#One is in input layer which getOutput is constant
#The other is in hidden layer which getOutput is var
class Neuron:
	def __init__(self,connectedNumber):
		self.weights=[]
		self.bias=0
		self.value=0
		self.connectedNumber=connectedNumber
		if connectedNumber>0:
			self.bias=(random.random()-0.5)*2
			for index in range(connectedNumber):
				self.weights.append((random.random()-0.5)*2)
	def getValue(self):
		return self.value
	#function for hidden layer neuron.
	def updateValue(self,inputSum,activateFunction):
		if self.connectedNumber==0:
			print('it is a neuron in input layer!Can not update')
			return 
		self.value = float(activateFunction.subs(Symbol('x'),inputSum))
		return self.value
	def getInputSum(self,upperLayer):
		if self.connectedNumber==0:
			print('it is a neuron in input layer!No Input sum')
			return []
		inputSum=0.0
		for index in range(0,len(upperLayer.neurons)):
			inputSum = inputSum+upperLayer.neurons[index].getValue()*self.weights[index]
		inputSum=inputSum+self.bias
		return inputSum
	def updateWeightsAndBias(self):
		pass
	def checkWeightsAndBias(self):
		pass
	def display(self):
		if self.connectedNumber==0:
			print('Input,value=%f'%(self.value))
		else:
			print('Hidden,weights=%s,bias=%.2f,value=%.2f'%(self.weights,self.bias,self.value))
		return
class NeuronLayer:
	def __init__(self,neurons=[]):
		self.neurons=neurons
	def display(self):
		for neuron in self.neurons:
			print('\t',end='')
			neuron.display()

class NeuralNetwork:

	def __init__(self,layerSize,activateFunction,updateRate,trainData):
		#layerSize [1,2] means first layer has one neuron,second layer has two neurons
		self.layerSize = layerSize
		self.activateFunction = activateFunction
		self.updateRate = updateRate
		#[[1,2,3],[2,3,4],[4,5,6]],three group,1:(1,2)in,(3)out,2:(2,3)in,(4)out,3:(4,5)in,(6)out
		self.trainData = trainData
		#init inputLayer		
		self.inputLayer=NeuronLayer([])
		for j in range(len(self.trainData[0])-1):
			self.inputLayer.neurons.append(Neuron(0))
		#init hiddenLayer
		self.hiddenLayers=[]
		for i in range(len(self.layerSize)):
			if i==0:
				upperLayer=self.inputLayer
			else:
				upperLayer=self.hiddenLayers[i-1]
			self.hiddenLayers.append(NeuronLayer([]))
			for j in range(self.layerSize[i]):
				self.hiddenLayers[i].neurons.append(Neuron(len(upperLayer.neurons)))
		#init outputNeuron
		upperLayer = self.hiddenLayers[-1]
		self.outputNeuron=Neuron(len(upperLayer.neurons))
	#good
	def calculateInputLayer(self,index):
		for i in range(len(self.trainData[index])-1):
			self.inputLayer.neurons[i].value=self.trainData[index][i]
	def calculateHiddenLayers(self):
		for i in range(len(self.layerSize)):
			if i==0:
				upperLayer=self.inputLayer
			else:
				upperLayer=self.hiddenLayers[i-1]
			for j in range(self.layerSize[i]):
				tmpNS = self.hiddenLayers[i].neurons[j]			
				inputSum = tmpNS.getInputSum(upperLayer)
				tmpNS.updateValue(inputSum,self.activateFunction)
	def calculateOutputNeuron(self):
		upperLayer = self.hiddenLayers[-1]
		inputSum = self.outputNeuron.getInputSum(upperLayer)
		self.outputNeuron.updateValue(inputSum,self.activateFunction)
	def getOutput(self,index):
		self.calculateInputLayer(index)
		self.calculateHiddenLayers()
		self.calculateOutputNeuron()
		return self.outputNeuron.value		
	def display(self):
		print("Input layer:")
		self.inputLayer.display()

		print("Hidden layer:")
		for index in range(len(self.hiddenLayers)):
			print('No.%d layer:'%(index))
			self.hiddenLayers[index].display()

		print("Output Neuron:",end='')
		self.outputNeuron.display()


















		


