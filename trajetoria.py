arquivo = open("v.txt", "r")
arquivoX = open("xConvertido.txt", "r")
arquivoY = open("yConvertido.txt", "r")
trajT = []
trajX = []
trajY = []
for line in arquivo:
    a, b, c = line.split()
    trajT.append(a)
arquivo.close()
for line in arquivoX:
    i = line.split()
    trajX.append(i)
for line in arquivoY:
    j = line.split()
    trajY.append(j)
