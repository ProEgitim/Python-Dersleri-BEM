import numpy as np
import matplotlib.pyplot as plt

x = np.arange(51)
y = np.arange(0,101,2)
z = x ** 3

plt.plot(x,y)

fig = plt.figure(figsize=(8,6))

axes1=fig.add_axes([0,0.1,0.8,0.8])
axes2=fig.add_axes([0.1,0.5,0.4,0.3])

plt.title("outherGraph - X vs Z Graph")
plt.title("innerGraph - X vs Y Graph")

plt.subplot(2,2,1)
plt.plot(x,z,"purple")
plt.subplot(2,2,2)
plt.plot(x,y,"red")

plt.show()