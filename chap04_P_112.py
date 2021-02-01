n = int(input())
x , y = 1 , 1
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L','R','U','D']

# 이동 계획을 하나 씩 확인
for plan in plans: #받아온 plans를 plan에 넣어 move type중에 어떤건지 하나씩 확인
    # 이동 후 좌표 구하기
    for i in range(len(move_type)): #0~3 반복하면 x좌표로 얼만큼 y좌표로 얼만큼이 나온다.
        if plan == move_type[i]: #plan(L,R,U,D중 하나)이 move_type[0~4]와 같다면
            nx = x + dx[i] #ex) plan이 R인경우 i==1 이므로 nx = 1 + dx[1], nx == 1
            ny = y + dy[i] #ex) paln이 R인경우 i==1 이므로 ny = 1 + dy[1], ny == 2
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x,y)

