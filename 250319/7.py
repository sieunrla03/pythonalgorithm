word = []
for i in range(0, 5):
  word.append(input())
shortest = word[0]
longest = word[0]
for i in range(1, len(word)):
  if len(word[i]) > len(longest):
    longest = word[i]
  if len(word[i]) < len(shortest):
    shortest = word[i]
print('longest :', longest)
print('shortest :', shortest)