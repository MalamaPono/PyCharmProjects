import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# saving one period of sin graph in matplotlib.
A = np.array([[1,2,3],[4,5,6],[3,2,3]])
X = np.arange(0,6.28,0.01)
Y = np.sin(X)
plt.plot(X,Y)
plt.savefig('sin.png')
