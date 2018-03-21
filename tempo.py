import time
a = 0.02
time.sleep(a)
count = 0
for i in range(77):
    count += a
    print("%.2f"%count)
