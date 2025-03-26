list_a = list(map(int, input().split()))

even_list = [x for x in list_a if x % 2 == 0]

print(even_list)