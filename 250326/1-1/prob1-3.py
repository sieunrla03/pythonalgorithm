# 추가할 문자열 입력
append_str = input("Enter the string to append...\n>> ")

# prob1-1.txt 읽기
with open("prob1-1.txt", "r") as file:
    lines = file.readlines()

# 입력 문자열을 마지막에 추가
lines.append(append_str + "\n")

# 수정된 내용을 prob1-3.txt로 저장
with open("prob1-3.txt", "w") as file:
    file.writelines(lines)

print("File append process has been finished")