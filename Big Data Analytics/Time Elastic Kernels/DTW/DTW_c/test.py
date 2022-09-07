import numpy as np
import DTW

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    A=np.array([[0],[0],[1],[1],[2],[3],[5],[2],[0],[1],[-0.1]])
    B=np.array([[0],[1],[2],[2.5],[3],[3.5],[4],[4.5],[5.5],[2],[0],[0],[.25],[.05],[0]])
    C=np.array([[4],[4],[3],[3],[3],[3],[2],[5],[2],[.5],[.5],[.5]])

    '''A=np.array([[0],[0],[1],[1],[2],[3],[5],[2],[0],[1],[-0.1]])
    B=np.array([[0],[1],[2],[2.5],[3],[3.5],[4],[4.5],[5.5],[2],[0],[0],[.25],[.05],[0]])
    C=np.array([[4],[4],[3],[3],[3],[3],[2],[5],[2],[.5],[.5],[.5]])'''
    degree=2
    print("dtw(A,B)=", DTW.distance(A, B, degree))
    print("dtw(A,C)=", DTW.distance(A, C, degree))
    print("dtw(B,C,)=", DTW.distance(B, C, degree))
        
    plt.plot(A, label='A')
    plt.plot(B, label='B')
    plt.plot(C, label='C')
    plt.legend()
    plt.show()
