numbers = list(map(int, input().split()))

if len(numbers) != 3:
    print('fail')
else:
    numbers.sort()
    print(numbers[1])