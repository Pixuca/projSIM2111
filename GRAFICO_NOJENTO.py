import random
import time
import matplotlib.pyplot as plt
import numpy as np


count = 1
mod = 1
for i in range(0, 999):
    count += mod
    print(count)
    #time.sleep(0.02)

vel = 0
acel = 0.5
tempo = 0
while (vel < 5):
    vel += acel
    #time.sleep(1)
    tempo += 1
    print(vel)
    print(tempo)
while (vel != 0):
    vel -= acel
    print(vel)
    if (vel == 0):
        acel = 0

plt.axis([0, 10, -2, 2])
plt.plot([0, 0.5, 0.5, 0.5, 0, 0, 0, 0 -0.5, -0.5, 0, 0, 0])
plt.plot([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.title('Aceleração em função do tempo')
plt.ylabel('a')
plt.xlabel('t(s)')
plt.show()
