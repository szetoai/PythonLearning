import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# normal distribution
n_array = np.random.normal(30, 5, 1000) # mu/mean of 30, sigma/stdev of 5, size of 1000
print(n_array)
# matrices
mtrx = np.matrix(np.ones((3, 3), dtype=int))
mtrx2 = mtrx + 5
product = np.dot(mtrx, mtrx2) # dot product
product2 = np.matmul(mtrx, mtrx2) # matrix multiplication
print(mtrx)
print(product)
print(product2)
# arange - like range but for arrays (list(range(1, 11)))
between_numbers = np.arange(0,10,2)
print(between_numbers)
# linspace/logspace - creates evenly spaced/log spaced items (min, max, items, endpoint (includes max))
print(np.linspace(1, 10, 20, endpoint=True))
print(np.logspace(1, 10, 20, endpoint=False))
# numpy stats
ex_stats = np.array([1,2,3,4,5])
print(np.min(ex_stats), np.max(ex_stats), np.mean(ex_stats), np.median(ex_stats), stats.mode(ex_stats), np.std(ex_stats), np.var(ex_stats), np.percentile(ex_stats, q=1))
# repeating arrays
print(np.tile(ex_stats, 2)) # repeats whole array twice
print(np.repeat(ex_stats, 2)) # repeats each element twice (1,1,2,2,3,3,4,4,5,5)
# linear algebra (what is this 0_o)
lin_alg = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(np.linalg.det(lin_alg))
# showing stats
# histogram
plt.hist(n_array, color="red", bins=50)
plt.show()
# plot
temps = np.array([90, 80, 75, 88, 100])
ice_creams = temps * 2 + 100
plt.plot(temps, ice_creams)
plt.xlabel("Temperatures")
plt.ylabel("Ice creams bought")
plt.title("Ice creams vs Temp")
plt.xticks(np.arange(60, 120, step=10))
plt.show()
# normal
sns.displot(n_array)
plt.show()