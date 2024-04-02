# 그대로 출력하기
while True:
    try:
        print(input())
    except EOFError:
        break
'''
EOFError는 예외가 발생했을 때, 즉 파일의 끝에 도달했을 때 반복문을 빠져나간다
'''