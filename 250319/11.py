# 비밀 숫자 입력 받기
secret_number = int(input())

if secret_number < 1:
    print(-1)  # 음수 입력 시 오류 메시지
else:
    attempts = 0  # 시도 횟수 초기화

    while True:
        try:
            # 사용자로부터 숫자 입력 받기
            guess = int(input())
            attempts += 1  # 시도 횟수 증가

            # 입력한 숫자와 비교
            if guess < secret_number:
                print("Up")
            elif guess > secret_number:
                print("Down")
            else:
                print("Correct")
                break  # 정답을 맞춘 경우 게임 종료

            # 시도 횟수 초과 시 게임 종료
            if attempts >= 10:
                print("End")
                break

        except ValueError:
            print("올바른 정수를 입력하세요.")  # 숫자가 아닌 입력 처리
