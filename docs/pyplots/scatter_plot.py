import matplotlib.pyplot as plt
import numpy as np

r = np.random.RandomState(42)
x = r.random_sample(10)
y0 = r.random_sample(10)
y1 = r.random_sample(10)

plt.scatter(x, y0, color='blue')
plt.scatter(x, y1, color='green')
plt.show()
