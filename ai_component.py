import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)


training_inputs = np.array([
    [0,0,1],
    [1,1,1],
    [1,0,1],
    [0,1,1]
])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

# Creates an array of random numbers between -1 & 1, in an array of 1 by 3 (aka 2d array with 3 values)
synaptic_weights = 2 * np.random.random((3, 1)) - 1

print('Random starting synaptic weights: ')
print(synaptic_weights)

for iteration in range(100000):
    input_layer = training_inputs

    # does multiplacation on matrixies
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    error = training_outputs - outputs

    ajustmants = error * sigmoid_deriv(outputs)

    synaptic_weights += np.dot(input_layer.T, ajustmants)

print("weights after traininig")

print(synaptic_weights)

print("output after training")
print(outputs)
