import matplotlib.pyplot as plt
import numpy as np

a = 15
b = 6
c = 100

theta = np.linspace(-2 * np.pi, 100, num=100)
k = np.linspace(0, 45, num=100)
r = k * (a+np.sin(theta*b+(k/c)))

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y, color='#CC0066')
plt.axis('off')
plt.show()
