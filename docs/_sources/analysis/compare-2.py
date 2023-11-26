import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

n = np.linspace(1, 20, 1000)
plt.plot(n,gamma(n+1))
plt.plot(n, 2**n)
plt.plot(n, 2*n**2)
plt.plot(n, 5*n*np.log2(n))
plt.plot(n, 20*n, '--')
plt.plot(n, 10*n, '--')

plt.ylim(0,500)
plt.xlim(0,15)

plt.text(6,  450,'n!')
plt.text(8, 450, '$2^n$')
plt.text(13, 450, '$2n^2$')
plt.text(12, 200, '$5n\cdot\log_{2}(n)$')
plt.text(14, 300, '$20n$')
plt.text(14, 120, '$10n$')

plt.title('Growth Rates')
plt.xlabel('Input size (n)')
plt.ylabel('Cost')

plt.show()