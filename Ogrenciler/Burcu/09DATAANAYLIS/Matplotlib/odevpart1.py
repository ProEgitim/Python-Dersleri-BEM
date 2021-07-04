import numpy as np
import matplotlib.pyplot as plt

x = np.arange(51)
y = np.arange(0,101,2)
z = x ** 3

plt.plot(x,y,z)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("X vs Y Graph")

plt.show()