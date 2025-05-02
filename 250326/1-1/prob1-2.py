# 문제 1-2: prob1-1.txt 파일의 내용을 출력

file_name = "prob1-1.txt"

print("Your inputs are below..")

try:
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"File '{file_name}' not found.")