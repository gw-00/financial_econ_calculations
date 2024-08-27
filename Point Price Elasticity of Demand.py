#calculate the point price elasticity of demand

import numpy as np
import matplotlib.pyplot as plt

#data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#plot
plt.plot(x, y, 'o')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Price Elasticity of Demand')
plt.show()

#calculate the slope
m = (y[1] - y[0]) / (x[1] - x[0])
print('The slope is', m)

