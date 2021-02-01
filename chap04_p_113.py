h = int(input())

count = 0

for i in range(h + 1): #시
    for j in range(60): #분
        for k in range(60): #초
            # 매시간 안에 '3'이 포함되어 있다면 카운트 증가
            # 문자열로바꿔서 03시20분35초 일때 ->032035 에서 3이 들어있는지 확인
            if '3' in str(i)+str(j)+str(k): 
                count += 1

print(count)