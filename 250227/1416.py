n = int(input())  # 단어 개수 입력
count = 0  # 그룹 단어 개수

for _ in range(n):
    word = input()
    seen = set()  # 등장한 문자 저장
    prev_char = ""  # 이전 문자 저장
    is_group_word = True  # 그룹 단어 여부

    for char in word:
        if char in seen and char != prev_char:
            is_group_word = False
            break
        seen.add(char)
        prev_char = char  # 이전 문자 업데이트

    if is_group_word:
        count += 1

print(count)  # 그룹 단어 개수 출력
