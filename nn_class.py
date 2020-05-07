import numpy as np

class NeuralNetwork():
    synaptic_weights = 0

    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((100,1)) - 1
        # print(self.synaptic_weights)

    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_deriv(self,x):
        return x * (1 - x)

    def train(self,training_inputs,training_outputs,training_itterations):
        for i in range(training_itterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            ajustmants = np.dot(training_inputs.T, error * self.sigmoid_deriv(output))
            self.synaptic_weights += ajustmants

    def think(self,inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output


if __name__ == "__main__":
    nn1 = NeuralNetwork()

    training_inputs = np.array([
        [0,0,1],
        [1,1,1],
        [1,0,1],
        [0,1,1]
    ])

    training_outputs = np.array([[0,1,1,0]]).T

    nn1.train(training_inputs,training_outputs, 10000)

    print("weight after traininig: ")
    print(nn1.synaptic_weights)

    a = str(input("Input 1: "))
    b = str(input("Input 2: "))
    c = str(input("Input 3: "))

    print("new  situation: input data = ", a,b,c)
    print("output data: ")
    print(nn1.think(np.array([a,b,c])))
