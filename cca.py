import matplotlib.pyplot as plt
import numpy as np
a = 200
b = 300

r = 300
x = np.arange(a-r,a+r+1)
y = np.sqrt(r**2 - (x-a)**2) + b
y2 = -y + 2*b


plt.plot(x,y)
plt.plot(x,y2)
plt.axis('equal')
plt.grid(color='1.2')

plt.show()