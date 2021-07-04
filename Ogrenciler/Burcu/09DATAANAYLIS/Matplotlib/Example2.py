import numpy as np
import matplotlib.pyplot as plt


x=np.arange(1,6)
y=np.arange(2,11,2)

plt.plot(x,y,"red")
###plt.show()

plt.plot(x,y)
plt.xlabel("X Değerleri")
plt.ylabel("Y Değerleri")
plt.title("x=y2 Grafiği")
###plt.show()

plt.subplot(2,2,1)
plt.plot(x,y,"red")
plt.subplot(2,2,2)
plt.plot(y,x,"blue")
plt.subplot(2,2,3)
plt.plot(y,y,"black")
plt.subplot(2,2,4)
plt.plot(x,y,"green")
plt.show()

