fileT = open("t.txt", "r")
fileX = open("x.txt", "r")
fileY = open("y.txt", "r")
t = []
xi = []
yi = []

for i in range(1001):
    a = fileT.readline()
    a = a.replace('\n', '')
    b = float(a)
    t.append(b)

for i in range(1001):
    a = fileX.readline()
    a = a.replace('\n', '')
    b = float(a)*100
    xi.append(b)

for i in range(1001):
    a = fileY.readline()
    a = a.replace('\n', '')
    b = float(a)*100
    yi.append(b)
