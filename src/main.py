import numpy as np
import matplotlib.pyplot as plt

def isPerfectSquare(r):
	s = np.sqrt(r)
	return s == np.floor(s)

def getAB(n,bound):
	return np.array([[a,b] for a in range(1,bound+1) for b in range(1,bound+1) if isPerfectSquare(a**2 + b**2 + n*a*b)]).T

# 

ab0=getAB(0, 100)
ab1=getAB(1, 100)
ab2=getAB(3, 40)

plt.grid()
plt.scatter(ab2[0],ab2[1])
# plt.scatter(ab1[0],ab1[1])
plt.show()