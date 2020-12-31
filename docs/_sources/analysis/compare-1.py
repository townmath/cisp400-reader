import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from matplotlib.patches import Rectangle

n = np.linspace(1, 55, 1000)
plt.plot(n,gamma(n))
plt.plot(n, 2**n)
plt.plot(n, 2*n**2)
plt.plot(n, 5*n*np.log2(n))
plt.plot(n, 20*n, '--')
plt.plot(n, 10*n, '--')

plt.ylim(0,2000)
plt.xlim(0,50)

plt.text(5,1800,'n!')
plt.text(12, 1800, '$2^n$')
plt.text(25, 1600, '$2n^2$')
plt.text(40, 1400, '$5n\cdot\log_{2}(n)$')
plt.text(45, 800, '$20n$')
plt.text(45, 300, '$10n$')

ax = plt.gca()
ax.add_patch(Rectangle((0,0),15,500,linewidth=1,linestyle='--',edgecolor='black',facecolor='none'))
plt.text(2, 510, 'zoom')

plt.title('Growth Rates')
plt.xlabel('Input size (n)')
plt.ylabel('Cost')

plt.show()