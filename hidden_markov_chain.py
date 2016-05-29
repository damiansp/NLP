from __future__ import division

def hmm_forward(Q, A, B, Obs, pi):
    ''' 
    Using the forward algorithm to compute the likelihood of a sequence of 
    observations (Obs) usint a Hidden Markov Model (HMM) with a given state
    transition probability matrix (A) and emission probability matrix (B).

    @param Q (list):                                    
      the set of N states [q1, q2, ..., qN]                                    
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
    @param pi (list):                                                          
      initial probability distribution (maps to Q)                            
    '''
    
# Stuff copied from existin markov_chain.py for reference (not to be used):
def markov_chain_prob(Q, A, Obs, B, pi, sequence):
    '''
    Define a (1st Order) Hidded Markov Chain 
    (e.g., transition probablities depend ONLY on current state)
    
    @param Q (list):
      the set of N states [q1, q2, ..., qN]
    @param A (matrix):
      the transition probability matrix:
      each a[i, j] represents the prob. of moving from state i to state j,
      s.t. sum[j](a[i, j]) = 1 for all i
    @param Obs (list):
      sequence of T observations
    @param B (matrix):
      sequence of observation likelihoods ("emission probabilities"), 
      b[i](o[t]); the probabilities of observations o[t] being generated from
      state i
    @param pi (list):
      initial probability distribution (maps to Q)
    @param sequence (list):
      list of consecutive states (in Q) for which the probability is to be
      determined
    '''
    pState = 1 # Initial probability for the sequence of states
    pObs   = 1 # Initial probability for the sequence of observations
    n = len(Obs)
    
    # Convert the sequence of states into indices for Obs
    for o in range(len(seqence)):
        sequence[s] = Obs.index(sequence[s])
    
    # Determine prob of initial state from pi
    p *= pi[sequence[0]]
    
    # For state in sequence:
    for state in range(len(sequence)):
        p *= A[sequence[state - 1]][sequence[state]]
    return p



# Example: Suppose we have an unknown sequence of consecutive days  (e.g.,
# { hot, warm, cold, ... } and wish to estimate the likelihood of a sequence of
# Max's daily ice cream purchases over the same time period.
# Determine the likelihoods of different ice cream sequences given known
# transisition probabilities given in A, and emission probabilities given in B.

# Tranisition         from-> to     
A = [[0.5, 0.4, 0.1], # h -> 
     [0.2, 0.6, 0.2], # w -> h w c
     [0.1, 0.3, 0.6]] # c ->
# Prob of n ice creams given:
#       h    w     c
B = [[0.1, 0.4, 0.94], # P(1 ice cream | { h,  w,  c })
     [0.4, 0.4, 0.05], #   2
     [0.5, 0.2, 0.01]] #   3
pi = [1/3, 1/3, 1/3]

# Possible ice cream amounts (hypotheses):
Obs1 = [3, 3, 1, 1, 2, 2, 3, 1, 3]
Obs2 = [3, 3, 1, 2, 3, 4, 3, 1, 2]
