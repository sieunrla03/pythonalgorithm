inp = int(input().strip())

if inp < 0:
    print(-1)
else:
    dis = 0
    if inp >= 150000:
        dis = 0.15
        print('15%')
    elif inp >= 100000:
        dis = 0.10
        print('10%')
    elif inp >= 50000:
        dis = 0.05
        print('5%')

result = round(inp * (1 - dis))
print(result)