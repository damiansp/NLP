from __future__ import division
import numpy as np

def hmm_forward(Q, A, B, Obs, pi):
    ''' 
    Using the forward algorithm to compute the likelihood of a sequence of 
    observations (Obs) usint a Hidden Markov Model (HMM) with a given state
    transition probability matrix (A) and emission probability matrix (B).

    @param Q (list):                                    
      the set of N states [q1, q2, ..., qN]                   
      *** NOTE: values should correspond to row indices in A ***
    @param A (matrix):                                                         
      the transition probability matrix:                                      
      each a[i, j] represents the prob. of moving from state i to state j, 
      s.t. sum[j](a[i, j]) = 1 for all i                                      
    @param B (matrix):                                                         
      sequence of observation likelihoods ("emission probabilities"),      
      b[i](o[t]); the probabilities of observations o[t] being generated from 
      state i                                                                 
    @param Obs (list):                                                         
      sequence of T observations
      ** NOTE: values should correspond to row indices in B ***
    @param pi (list):                                                          
      initial probability distribution (maps to Q)             

    @return lattice (matrix)
      An N x T matrix, where N = len(Q) and T = len(Obs), with each cell's 
      value representing the (cumulative) probability of being at each state 
      at each time step (sequential observation); e.g. lattice[q, t] is the
      (relative) probability of being at state q after the first 1 ~ t - 1 
      observations.  Hence, the most likely sequence of states may be inferred
      from the highest value in each column (time step).
    '''
    
    # make sure A and B are numpy arrays
    A = np.array(A)
    B = np.array(B)

    N = len(Q)
    T = len(Obs)
    lattice = np.zeros(shape = (N, T))

    # Initialize first column of lattice (time = 0; start)
    for q in range(N):
        lattice[q, 0] = pi[q] * B[Obs[0], q]

    # Fill in the rest of the lattice
    for t in range(1, T):
        for q in range(N):
            node_val = 0

            for q2 in range(N):
                # alpha = the value at the nodes in the previous column
                alpha = lattice[q2, t -1]
                # a = the probability of being at current state given a
                # previous state
                a = A[q2, q]
                # b = the probability of a given observation given the current
                # state
                b = B[Obs[t], q2]
                # The probability of being at a current state given a prior
                # state is thus alpha * a * b; sum over all possible prior
                # states
                node_val += (alpha * a * b)

            lattice[q, t] = node_val

    return lattice

# Example: Suppose we have an unknown sequence of consecutive days  (e.g.,
# { hot, warm, cold, ... } but have receipts for Max's daily ice cream
# purchases over the same time period.
# Determine the likelihoods of different ice cream sequences given known
# transisition probabilities given in A, and emission probabilities given in B.

Q = [0, 1, 2] # corresponds to ROW INDICES in A ('hot', 'warm', 'cold')

# State Transitions   from-> to     
A = [[0.5, 0.4, 0.1], # h -> 
     [0.2, 0.6, 0.2], # w -> h w c
     [0.1, 0.3, 0.6]] # c ->

# Prob of n ice creams given:
#       h    w     c
B = [[0.1, 0.4, 0.94], # P(1 ice cream | { h,  w,  c })
     [0.4, 0.4, 0.05], #   2
     [0.5, 0.2, 0.01]] #   3
pi = [1/3, 1/3, 1/3]

# Possible ice cream amounts (hypotheses)
# NOTE: Values correspond to ROW VALUES in B, e.g., 0 means B[0,] (1 ice cream)
Obs1 = [2, 2, 0, 0, 1, 1, 2, 0, 2]
Obs2 = [2, 2, 0, 1, 2, 2, 2, 0, 1]

H1 = hmm_forward(Q, A, B, Obs1, pi)
H2 = hmm_forward(Q, A, B, Obs2, pi)

print 'Hypothesis 1 Probability Matrix:\n', H1
print 'Hypothesis 2 Probability Matrix:\n', H2

# TO DO:
# Hand check a small set to make sure calculations came out correctly
# See if vectorization can be done to improve efficiency
