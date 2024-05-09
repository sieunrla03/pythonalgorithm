# 최댓값
max = 0
max_row, max_col = 0, 0

table = [list(map(int, input().split())) for _ in range(9)]

for row in range(9):
    for col in range(9):
        if max <= table[row][col]:
            max_row = row + 1
            max_col = col + 1
            max = table[row][col]
print(max)
print(max_row, max_col)