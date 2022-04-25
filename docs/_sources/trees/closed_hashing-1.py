import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, 1, 100)
plt.plot(n, 1/(1-n) -1)

plt.ylim(0,20.5)
plt.xlim(0,0.96)

plt.title('Collision growth vs. load factor')
plt.xlabel('Load factor')
plt.ylabel('Average # of collisions')
plt.xticks(np.arange(0, 1, step=0.1))
plt.yticks(np.arange(0, 20.5, step=2))

plt.show()