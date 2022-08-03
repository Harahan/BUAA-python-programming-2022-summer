import numpy as np
from numpy.linalg import *
na = []
for i in range(4):
	na.append(list(map(int, input().split())))
na = np.array(na)
print(int(det(na)))
