#문자열을 입력받아 하나하나 숫자로 변환한뒤 곱하기와 더하기를 통해 제일 큰 수 만들기

data = input()
#첫번째 문자열을 정수형으로 바꿔서 대입
result = int(data[0])

for i in range(1, len(data)): #1부터 len(data)-1 까지 i에 대입
    num = int(data[i])
    # result와 num의 값이 둘다 0보다 크다면 곱하기
    if result > 0 and num > 0:
        result *= num
    # 하나라도 0이라면 더하기
    else:
        result += num
print(result)

    
