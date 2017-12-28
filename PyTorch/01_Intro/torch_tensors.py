import numpy as np
import torch

# init Tensors
x = torch.Tensor(5, 3) # (dims)
print('x:\n', x)

x = torch.rand(5, 3) # all on [0, 1)
print(x)

x = torch.zeros(3, 3)
print(x)

x = torch.ones(3, 3)
print(x)

x = torch.Tensor(3, 4).fill_(5) # all _ methods are in-place
print(x)

x = torch.Tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(x)


# To/from np.arrays
a = np.random.rand(5, 3)
x = torch.from_numpy(a)
print(x)
print(x.numpy())


# Declaring/casting data types
