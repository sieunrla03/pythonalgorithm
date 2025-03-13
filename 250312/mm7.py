inp = int(input())
if inp >= 80 and inp <= 100:
    print('A')
elif inp >= 60 and inp  < 80:
    print('B')
elif inp < 60 and inp >= 0:
    print('C')
elif inp <= 0 or inp > 100:
    print('-1')