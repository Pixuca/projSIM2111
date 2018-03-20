'''K = int(input())
a = 1
b = 1

for i in range (0, K):
	if i == 0:
		print("0", end=" ")
	else:
		soma = a;
		a = b;
		b = soma + b;
		if i == K - 1:
			print(soma)
		else:
			print(soma, end=" ")'''

fibo = int(input())
b = 1
for i in range(0, fibo):
    if i == 0: print("0", end=" ")

    else:
        soma = 1
        b += soma
        if i == fibo - 1:
            print(soma)
        else:
            print(soma, end=" ")
