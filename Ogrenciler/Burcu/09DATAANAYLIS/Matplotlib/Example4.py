import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,6)
y=np.arange(2,11,2)

fig = plt.figure()

axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,x**2,color="red",marker="o",markersize=20,markerfacecolor="black")

plt.show()