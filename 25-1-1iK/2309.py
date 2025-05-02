일곱 난쟁이
N = []
for i in range(9):
    N.append(int(input()))

N.sort()

sumn = sum(N)

for i in range(len(N)):
    for j in range(i + 1, len(N)):
        if sumn - N[i] - N[j] == 100:
            for k in range(len(N)):
                if k == i or k == j:
                    pass
                else:
                    print(N[k])
            exit()

