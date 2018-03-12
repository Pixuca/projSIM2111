import matplotlib.pyplot as plt
import numpy as np
from pypy import *

vel = 1
dist = 30
a = np.arange(vel, dist)

plt.plot(a, a**2)
plt.title('Gráfico 1 (Velocidade x Tempo)')
plt.ylabel('Distância (mm)')
plt.xlabel('Tempo (s)')
plt.show()
