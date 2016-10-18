# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Generate data for the plot
x = np.linspace(0, 1, 21)
y0 = np.sin(2*np.pi*x)
y1 = np.cos(2*np.pi*x)

# Generate the plot
plt.plot(x, y0)
plt.plot(x, y1)
plt.show()
