#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.spatial.distance import cdist
import numpy as np
'''try:
    from numba import jit
except ImportError:
    print('Warning, Numba not installed. Performance will be significantly slower')
    jit = lambda x: x

@jit'''
def dtw_distance(distances):
    '''calculate minimum cumulative distance'''
    n,m=np.shape(distances)
    DTW = np.zeros((n+1,m+1))
    DTW[:, 0] = np.inf
    DTW[0, :] = np.inf    
    DTW[0, 0] = 0
    for i in range(1, DTW.shape[0]):
        for j in range(1, DTW.shape[1]):
            DTW[i, j] = distances[i-1, j-1] + min(DTW[i-1, j],  # insertion
                                              DTW[i, j-1],  # deletion
                                              DTW[i-1, j-1] #match
                                             )
    return DTW

def backtrack(DTW):
    '''compute DTW backtrace
    DTW: a matrix of cumulative DTW paths
    returns (p, q): x and y index lists of the optimal DTW path'''
    i, j = DTW.shape[0] - 1, DTW.shape[1] - 1
    p, q = [i], [j]
    while i > 0 and j > 0:
        local_min = np.argmin((DTW[i - 1, j - 1], DTW[i, j - 1], DTW[i - 1, j]))
        if local_min == 0:
            i -= 1
            j -= 1
        elif local_min == 1:
            j -= 1
        else:
            i -= 1
        p.append(i)
        q.append(j)
    p.reverse()
    q.reverse()
    return p, q

def dtw(a, b, distance_metric='sqeuclidean'):
    '''perform dynamic time warping on two matrices a and b
    '''
    distance = cdist(a, b, distance_metric)
    cum_min_dist = dtw_distance(distance)
    trace_x, trace_y = backtrack(cum_min_dist)
    return cum_min_dist, trace_x, trace_y

# Simple test
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    A=np.array([[0],[0],[1],[1],[2],[3],[5],[2],[0],[1],[-0.1]])
    B=np.array([[0],[1],[2],[2.5],[3],[3.5],[4],[4.5],[5.5],[2],[0],[0],[.25],[.05],[0]])
    C=np.array([[4],[4],[3],[3],[3],[3],[2],[5],[2],[.5],[.5],[.5]])
    
    print("ddtw(A,B)=", dtw(A,B)[0][-1,-1])
    print("dtw(A,C)=", dtw(A,C)[0][-1,-1])
    print("dtw(B,C)=", dtw(B,C)[0][-1,-1])
        
    plt.plot(A, label='A')
    plt.plot(B, label='B')
    plt.plot(C, label='C')
    plt.legend()
    plt.show()
