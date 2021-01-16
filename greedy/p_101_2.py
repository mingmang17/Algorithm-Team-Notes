#1이 될때까지 나누거나 1씩 빼기 그 과정이 제일 적은 수 구하기

#n,k 를 공백으로 구분하여 입력받기
n , k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될때까지 1씩 빼기
    target = (n//k) * k
    result += (n - target)
    n = target
    #n을 k로 나눌수 없을 때 반복문 탈출
    if n<k:
        break
    #n이 k로 나누어 떨어지는 수가 되면 n을 k로 나누고 result에 +1
    n//=k
    result +=1

#n이 k보다 작아졌을 때 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
 
