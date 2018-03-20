import random
import os
import time


x = 780
real = x/9
x2 = 350
count = 0
real2 = real
while (real2 <= x2):
    real2 += real
    count += 1
    print("Distância entre o objeto e o início do campo: %.2fm" % count)
print("A cada %.2f pixels, um metro em X é caminhado." % real)
