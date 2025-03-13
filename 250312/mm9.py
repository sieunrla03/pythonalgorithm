input_line = input()
parts = input_line.split()
a = int(parts[0])
b = parts[1]  # 연산자
c = int(parts[2])

result = 0

if b == '+':
    result = a + c
elif b == '-':
    result = a - c
elif b == '*':
    result = a * c
elif b == '/':
    if b == o:
        print('can not divide by 0')
    else:
        resut = a / c
print(a, b, c, '=', result)
    