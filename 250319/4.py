def getround(radius):
    return 2 * 3.14 * radius

def getarea(radius):
    return 3.14 * radius ** 2

n = int(input())
if n <= 0:
  print('-1')
else:
  print(f"round : {getround(n):.2f}")
  print(f"area : {getarea(n):.2f}")