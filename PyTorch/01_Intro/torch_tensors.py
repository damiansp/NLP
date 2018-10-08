import numpy as np
import torch
from torch.autograd import Variable

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
x = torch.FloatTensor([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
print(x)

x = x.long()
print(x)
print(x.size())


# Tensor Operations
x = torch.rand(3, 4)
print(x)

y = torch.add(x, x)
print(y)

z = y + y
print(z)

print(torch.sum(x, dim=0)) # col sums



# Indexing
x = torch.FloatTensor([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
print(x[:2, :2])
print(x[0][1])
x[0, 0] = 8
x[1][2] = 12
print(x)

indices = torch.LongTensor([0, 2])
print(torch.index_select(x, dim=0, index=indices)) # rows 0 and 2
print(torch.cat([x, x, x], dim=0)) # v-stack


# Common Linear Algebra Functions
print('LA' + '-' * 73)

x = torch.rand(3, 4)
print(x)
print(torch.transpose(x, dim0=0, dim1=1))
print(torch.add(x, x))

# Matrix mult
print(torch.mm(x, torch.transpose(x, dim0=0, dim1=1)))

# Trace
print(torch.trace(x))


# PyTorch Variables
x = Variable(torch.LongTensor([2]), requires_grad=True)
z = 3 * x
print(z)
print(z.data)
print(z.grad_fn)  # formerly z.creator

z.backward()
print(x.grad)


# CUDA Tensors
print(torch.cuda.is_available())
if torch.cuda.is_available():
    a = torch.rand(3, 3).cuda()
    print(a)

    # NOTE: cuda tensors and regular tensors cannot interact with each other
    # To get them to interact, the tensors must be available on the same device:
    a = a.cpu() # copy to CPU
    b = torch.rand(3, 3)
    print(a + b)


    
