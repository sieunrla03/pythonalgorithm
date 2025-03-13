inp = int(input())
a = inp %2
if a == 0 and inp >= 0:
    print('even')
elif a != 0 and inp >= 0:
    print('odd')
elif inp <= 0:
    print('-1')
