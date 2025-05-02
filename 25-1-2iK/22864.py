# 피로도
A, B, C, M = map(int, input().split()) # 입력받기

T = 0 # 피로도
W = 0 # 최대 작업량

for i in range(24): # 하루는 24시간이므로 24번 반복
    if M < T: # 피로도가 M 넘을경우 번아웃으로 작업량 0
        print(0)
    else:
        if T + A <= M: # 일 할 수 있는 경우
            T += A # A만큼 피로도 더하기, B만큼 작업량 추가
            W += B
        else:
            if T - C >= 0: # 일을 할 수 없는 경우
                T -= C # 휴식으로 피로도가 C만큼 감소, 그 값이 0 이상일 경우 피로도가 C만큼 감
            else:
                T = 0 # 휴식으로 피로도가 음수인 경우, 피로도 0
print(W)