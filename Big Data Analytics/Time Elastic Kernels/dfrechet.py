import unittest, doctest, math, random
import numpy as np
from scipy.spatial.distance import cdist

##############################################################################
# Classical computation of Discrete Frechet distance
##############################################################################

def euclideanDist(x,y):
    u=x-y
    return np.sqrt(np.sum(u*u))

def recursive(dynamicProgrammingArray,i,j,P,Q):
    """
    Computes the Frechet distance between @P and @Q in @dynamicProgrammingArray by a simple dynamic programming recursion over @i and @j

    >>> P = [(1,1),(1,2)]
    >>> Q = [(2,1),(2,2)]
    >>> dynamicProgrammingArray = np.ones((len(P),len(Q)))
    >>> dynamicProgrammingArray = np.multiply(dynamicProgrammingArray,-1)
    >>> recursive(dynamicProgrammingArray,len(P)-1,len(Q)-1,P,Q)
    1.0

    """
    if dynamicProgrammingArray[i,j] > -1:
        return dynamicProgrammingArray[i,j]
    elif i == 0 and j == 0:
        dynamicProgrammingArray[i,j] = euclideanDist(P[0],Q[0])
    elif i > 0 and j == 0:
        dynamicProgrammingArray[i,j] = max(
            recursive(dynamicProgrammingArray,i-1,0,P,Q),
            euclideanDist(P[i],Q[0]))
    elif i == 0 and j > 0:
        dynamicProgrammingArray[i,j] = max(
            recursive(dynamicProgrammingArray,0,j-1,P,Q),
            euclideanDist(P[0],Q[j]))
    elif i > 0 and j > 0:
        dynamicProgrammingArray[i,j] = max(
            min(
                recursive(dynamicProgrammingArray,i-1,j,P,Q),
                recursive(dynamicProgrammingArray,i-1,j-1,P,Q),
                recursive(dynamicProgrammingArray,i,j-1,P,Q)),
            euclideanDist(P[i],Q[j]))
    else:
        dynamicProgrammingArray[i,j] = float("inf")
    return dynamicProgrammingArray[i,j]

def frechet(P,Q):
    """ Computes the discrete frechet distance between two polygonal lines
    Algorithm: http://www.kr.tuwien.ac.at/staff/eiter/et-archive/cdtr9464.pdf
    P and Q are arrays of 2-element arrays (points)

    >>> P = [(1,1),(1,2)]
    >>> Q = [(2,1),(2,2)]
    >>> computation(P,Q)
    1.0

    """
    dynamicProgrammingArray = np.ones((len(P),len(Q)))
    dynamicProgrammingArray = np.multiply(dynamicProgrammingArray,-1)
    d = recursive(dynamicProgrammingArray,len(P)-1,len(Q)-1,P,Q)
    return d



# Simple test
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    A=np.array([[0,0],[0,0],[1,1],[1,1],[2,0],[3,0],[5,1],[2,1],[0,1],[1,0],[-0.1,0]])
    B=np.array([[0,0],[1,0],[2,1],[2.5,1],[3,1],[3.5,0],[4,0],[4.5,0],[5.5,0],[2,0],[0,0],[0,0],[.25,0],[.05,0],[0,0]])
    C=np.array([[4,0],[4,0],[3,0],[3,0],[3,0],[3,0],[2,0],[5,0],[2,0],[.5,0],[.5,0],[.5,0]])
    
    print("frechet(A,B)=", frechet(A,B))
    print("frechet(A,C)=", frechet(A,C))
    print("frechet(B,C)=", frechet(B,C))
        
    plt.plot(A, label='A')
    plt.plot(B, label='B')
    plt.plot(C, label='C')
    plt.legend()
    plt.show()