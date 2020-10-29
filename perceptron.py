import numpy as np
import pandas as pd

df = pd.read_csv('park.csv')

features = df[['MDVP:Jitter(Abs)','Jitter:DDP','MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','D2','PPE']]
X = features.to_numpy()
Y = df[['status']].to_numpy()

def signm(x):
    return 1/(1+np.exp(-x))

def d_signm(x):
    return x*(1-x)

epoch=500 #Setting training iterations
lr=0.1 #Setting learning rate
inputlayer_neurons = X.shape[1] #number of features in data set
hiddenlayer_neurons = 3 #number of hidden layers neurons
output_neurons = 1 #number of neurons at output layer
#weight and bias initialization
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))
for i in range(epoch):

#Forward Propogation
    hidden_layer_input1=np.dot(X,wh)
    hidden_layer_input=hidden_layer_input1 + bh
    hiddenlayer_activations = signm(hidden_layer_input)
    output_layer_input1=np.dot(hiddenlayer_activations,wout)
    output_layer_input= output_layer_input1+ bout
    output = signm(output_layer_input)
    #Backpropagation
    E = Y-output
    slope_output_layer = d_signm(output)
    slope_hidden_layer = d_signm(hiddenlayer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) *lr
    bout += np.sum(d_output, axis=0,keepdims=True) *lr
    wh += X.T.dot(d_hiddenlayer) *lr
    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr

print (output)
#print(E)
