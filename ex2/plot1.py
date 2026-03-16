#same as plot.pybut allows to see up to 30 time batches
import numpy as np
import matplotlib.pyplot as plt

def Show_data1(x,L,s="data"):
    for i in range(30):
        if i%3==0:
            col='blue'
        if i%3==1:
            col='red'
        if i%3==2:
            col='green'
        plt.plot(np.arange(i*L,(i+1)*L),x[i], color=col)
    plt.title(s)
    plt.xlabel("time")
    plt.show()