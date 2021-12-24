import torch
import torch.nn as nn
import torch.nn.functional as F


class MultilayerPerceptron(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        '''
        Args:
          input_dim, hidden_dim, output_dim (int): number of perceptrons in each
            layer (only one hidden layer).
        '''
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x_in, apply_softmax=False):
        '''
        Forward Pass
        Args:
          x_in: (torch.Tensor): input tensor, .shape should be 
            (batch, input_dim)
          apply_softmax (bool): apply softmax? F if used with x-entropy
        Returns:
          tensor with shape (batch, output_dim)
        '''
        intermediate = F.relu(self.fc1(x_in))
        output = self.fc2(intermediate)
        if apply_softmax:
            output = F.softmax(output, dim=1)
        return output


BATCH = 2
INPUT = 3
HIDDEN = 100
OUTPUT = 4

mlp = MultilayerPerceptron(INPUT, HIDDEN, OUTPUT)
print(mlp)


# Test with random inputs
def describe(x):
    print(f'Type: {x.type()}')
    print(f'Shape: {x.shape}')
    print(f'Values:\n {x}')


x_input = torch.rand(BATCH, INPUT)
y_output = mlp(x_input)
describe(x_input)
describe(y_output)



# Surname classifation with FFNN
