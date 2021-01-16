#1이 될때까지 나누거나 1씩 빼기 그 과정이 제일 적은 수 구하기

n , k = map(int, input().split())
result =0

#n을 k로 나눌수 있을때 까지 나누기
while n >= k : 
    while n%k !=0:
        n -= 1
        result +=1
    n /= k
    result+=1

while n > 1:
    n-=1
    result+=1

print(result)
