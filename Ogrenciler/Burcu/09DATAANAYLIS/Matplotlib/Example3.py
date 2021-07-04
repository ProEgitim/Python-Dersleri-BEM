import numpy as np
import matplotlib.pyplot as plt

###fig = plt.figure(figsize=(8,4))

###axes1=fig.add_axes([0.1,0.1,0.8,0.8])
###axes2=fig.add_axes([0.4,0.5,0.4,0.3])

###plt.show()

###fig,axes=plt.subplots(nrows=2,ncols=2)
###plt.tight_layout()
###plt.show()

x = range(1, 2)

fig = plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,x**2,color="red",lw=9,ls="-.")

plt.show()

### neden çalışmadı