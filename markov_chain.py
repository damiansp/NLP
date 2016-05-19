from __future__ import division

def markov_chain_prob(Q, A, pi, sequence):
    '''
    Define a Markov Chain
    
    @param Q (list):
      the set of N states [q1, q2, ..., qN]
    @param A (matrix):
      the transition probability matrix:
      each a[i, j] represents the prob. of moving from state i to state j,
      s.t. sum[j](a[i, j]) = 1 for all i
    @param pi (list):
      initial probability distribution (maps to Q)
    @param sequence (list):
      list of consecutive states (in Q) for which the probability is to be
      determined
    '''
    p = 1 # Probability
    N = len(Q)
    
    # Convert the sequence of states into indices for Q
    for s in range(len(sequence)):
        sequence[s] = Q.index(sequence[s])
    
    # Determine prob of initial state from pi
    p *= pi[sequence[0]]
    
    # For state in sequence:
    for state in range(len(sequence)):
        p *= A[sequence[state - 1]][sequence[state]]
    return p



# Example: Suppose we have consecutive days from { hot, warm, cold } with the
# transition probabilities given in A.  What is the probability of each of the
# following sequences?
Q = ['hot', 'warm', 'cold']
A = [[0.5, 0.4, 0.1], # h -> 
     [0.2, 0.6, 0.2], # w -> h w c
     [0.1, 0.3, 0.6]] # c ->
pi = [1/3, 1/3, 1/3]

seq1 = ['hot', 'hot',  'hot',  'hot',  'hot']
seq2 = ['hot', 'warm', 'cold', 'warm', 'hot']
seq3 = ['hot', 'cold', 'hot',  'cold', 'hot']

print 'P(seq1) =', markov_chain_prob(Q, A, pi, seq1)
print 'P(seq2) =', markov_chain_prob(Q, A, pi, seq2)
print 'P(seq3) =', markov_chain_prob(Q, A, pi, seq3)
