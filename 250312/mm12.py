N = int(input().strip())
coins = [500, 100, 50, 10]
change = []

for coin in coins:
    change.append(N // coin)
    N %= coin

print(" ".join(map(str, change)))