import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


# 1 method
# fig, axs = plt.subplots(6, 3)
#(fig, [ax1, ax2, ax3, ax4, ax5]) = plt.subplots(2,2) 
# 3 method
#fig = plt.figure()
#ax1 = fig.add_subplot(3,2,4)

fig, ax = plt.subplots(3,2)
x=range(5,10)
y=range(20,40,4)
ax[0,0].plot(x,y,"ro--")
ax[0,0].set_xlim(0,10)
ax[0,0].set_ylim(0,40)
ax[0,0].tick_params(which="both", width=12)
ax[0,0].tick_params(which="minor", lenght=2, color="r")
ax[0,0].tick_params(which="major", lenght=6, color="g")

ax[0,0].xaxis.set_minor_locator(MultipleLocator(0.5))
ax[0,0].yaxis.set_minor_locator(MultipleLocator(5))
ax[0,0].xaxis.set_major_locator(MultipleLocator(4))
ax[0,0].yaxis.set_major_locator(MultipleLocator(10))

ax[2,1].plot(y,x,"yx-")
ax[1,1].bar(x,y,color="g")
plt.tight_layout()

plt.show()