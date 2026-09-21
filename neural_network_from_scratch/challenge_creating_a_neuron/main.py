import numpy as np

# Fix the seed for reproducibility
np.random.seed(10)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

class Neuron:
    def __init__(self, n_inputs):
        # 1. Initialize weights and bias with random values
        self.weights = ___
        self.bias = ___

    def activate(self, inputs):
        # 2. Compute the weighted sum using dot product and add bias
        input_sum_with_bias = ___
        # 3. Apply the sigmoid activation function
        output = ___

        return output

# Create a neuron with 3 inputs
neuron = Neuron(3)
# Generate inputs for the neuron
neuron_inputs = np.array([0.5, 0.2, -0.8])
# Pass the inputs to the created neuron
neuron_output = neuron.activate(neuron_inputs)

print(f'Output of the neuron is {neuron_output:.3f}')