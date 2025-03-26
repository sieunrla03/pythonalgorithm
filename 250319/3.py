n = int(input())

if n > 100 or n < 0:
    exit()
else:
    total = sum(i for i in range(5, n + 1, 5))
    print(total)