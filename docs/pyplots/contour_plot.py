# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter

x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
r = np.random.RandomState(42)
z = gaussian_filter(r.random_sample([50, 50]), sigma=5, mode='wrap')
z -= np.min(z)
z /= np.max(z)

plt.contour(x, y, z)
plt.colorbar()
plt.show()
